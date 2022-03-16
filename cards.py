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


class Deck:
    """Deck class"""

    def __init__(self) -> None:
        self.cards = []

    def add_standard_52_cards_deck(self) -> None:
        """Add standard 52 cards dek to deck instance"""

        for colour in list(CardColour):
            for value in list(CardValue):
                self.cards.append(Card(colour, value))

    def suffle(self) -> None:
        """Suffle the cards list in deck"""
        shuffle(self.cards)

    def take_card(self) -> Card:
        """Take and return last card from deck

        Returns:
            Card: Card whitch was taken from deck
        """
        return self.cards.pop()


def main():
    """function writen for module tests"""
    deck = Deck()
    deck.add_standard_52_cards_deck()
    deck.suffle()
    for index, card in enumerate(deck.cards, start=1):
        print(f'{index}: {card}')

    print(f'{deck.cards[1]} = {deck.cards[2]}: {deck.cards[1] == deck.cards[2]}')
    print(f'{deck.cards[1]} = {deck.cards[1]}: {deck.cards[1] == deck.cards[1]}')

    print(f'{deck.cards[1]} != {deck.cards[2]}: {deck.cards[1] == deck.cards[2]}')
    print(f'{deck.cards[1]} != {deck.cards[1]}: {deck.cards[1] == deck.cards[1]}')


if __name__ == '__main__':
    main()
