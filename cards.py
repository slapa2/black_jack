"""Playing card module"""

from enum import Enum
from random import shuffle

class CardColour(Enum):
    """Card colour enum type"""
    SPADE = 'Spade'
    HEART = 'Heart'
    DIMOND = 'Diamond'
    CLUB = 'Club'


class CardValue(Enum):
    """Card value enum type"""
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '10'
    JACK = 'Jack'
    QUEEN = 'Queen'
    KING = 'King'
    ACE = 'Ace'


class Card:
    """Card item class"""

    def __init__(self, colour: CardColour, value: CardValue) -> None:
        self.colour = colour
        self.value = value

    def __str__(self) -> str:
        return f'{self.colour.value} {self.value.value}'

    def __cmp__(self, other) -> bool:
        return (self.colour == other.colour) and (self.value == other.value)


class CardsList:
    """Class representing any list of cards"""
    def __init__(self) -> None:
        self.cards = []

    def __str__(self) -> str:
        ret = [f'{index}: {card}' for index, card in enumerate(self.cards, start=1)]
        return '\n'.join(ret)

    def suffle(self) -> None:
        """Suffle the cards list in deck"""
        shuffle(self.cards)

    def take_last_card(self) -> Card:
        """Take and return last card from deck

        Returns:
            Card: Card whitch was taken from deck
        """
        return self.cards.pop()

    def add_card(self, card: Card) -> None:
        """Add a car to cards list

        Args:
            card (Card): Card to add
        """
        self.cards.append(card)


class Deck(CardsList):
    """Deck class"""

    def add_standard_52_cards_deck(self) -> None:
        """Add standard 52 cards dek to deck instance"""
        for colour in list(CardColour):
            for value in list(CardValue):
                self.cards.append(Card(colour, value))


class Heand(CardsList):
    """Player heand class"""
    def add_card_form_deck(self, deck: Deck) -> None:
        """Adding card from deck to heand

        Args:
            deck (Deck): Deck
        """
        self.add_card(deck.take_last_card())

    def add_cards_from_deck(self, deck: Deck, cards_number: int) -> None:
        """Adding number of cards form deck to heand

        Args:
            deck (Deck): Deck
            cards_number (int): number of cards to add to heand
        """
        for _ in range(cards_number):
            self.add_card_form_deck(deck)


def main():
    """function writen for module tests"""
    deck = Deck()
    deck.add_standard_52_cards_deck()
    deck.suffle()
    print(deck)

    print(f'{deck.cards[1]} = {deck.cards[2]}: {deck.cards[1] == deck.cards[2]}')
    print(f'{deck.cards[1]} = {deck.cards[1]}: {deck.cards[1] == deck.cards[1]}')

    print(f'{deck.cards[1]} != {deck.cards[2]}: {deck.cards[1] == deck.cards[2]}')
    print(f'{deck.cards[1]} != {deck.cards[1]}: {deck.cards[1] == deck.cards[1]}')

    player_heand = Heand()
    player_heand.add_cards_from_deck(deck, 5)
    print(player_heand)
    player_heand.add_card_form_deck(deck)
    print(player_heand)
    print(deck)



if __name__ == '__main__':
    main()
