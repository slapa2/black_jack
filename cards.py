"""Playing card module"""

from enum import Enum
from random import shuffle

from typing import List


class CardColour(Enum):
    """Card colour enum type"""
    SPADE = '♠'
    HEART = '♥'
    DIMOND = '♦'
    CLUB = '♣'


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
    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'
    ACE = 'A'


class Card:
    """Card item class"""

    def __init__(self, colour: CardColour, value: CardValue) -> None:
        self.colour = colour
        self.value = value

    def __str__(self) -> str:
        return f'{self.value.value}{self.colour.value}'

    def __eq__(self, other) -> bool:
        return all([
            self.colour == other.colour,
            self.value == other.value
        ])


class CardsList:
    """Class representing any list of cards"""

    def __init__(self) -> None:
        self.cards = []

    def __str__(self) -> str:
        ret = [f'{card}' for index, card in enumerate(self.cards, start=1)]
        return ', '.join(ret)

    def shuffle(self) -> None:
        """Shuffle the cards list in deck"""
        shuffle(self.cards)

    def take_last_card(self) -> Card:
        """Take and return last card from deck

        Returns:
            Card: Card which was taken from deck
        """
        if len(self.cards) == 0:
            raise NoCardsException
        return self.cards.pop()

    def add_card(self, card: Card) -> None:
        """Add a car to cards list

        Args:
            card (Card): Card to add
        """
        self.cards.append(card)

    def add_cards(self, cards: List[Card]):
        """add from list of cards"""
        self.cards.extend(cards)

    def remove_cards(self) -> List[Card]:
        """remove all cards from CardList"""
        tmp = self.cards
        self.cards = []
        return tmp


class Deck(CardsList):
    """Deck class"""

    def add_standard_52_cards_deck(self) -> None:
        """Add standard 52 cards dek to deck instance"""
        for colour in list(CardColour):
            for value in list(CardValue):
                self.cards.append(Card(colour, value))


class Hand(CardsList):
    """Player hand class"""

    def add_card_from_deck(self, deck: Deck) -> None:
        """Adding card from deck to hand

        Args:
            deck (Deck): Deck
        """
        self.add_card(deck.take_last_card())

    def add_cards_from_deck(self, deck: Deck, cards_number: int) -> None:
        """Adding number of cards form deck to hand

        Args:
            deck (Deck): Deck
            cards_number (int): number of cards to add to hand
        """
        for _ in range(cards_number):
            self.add_card_from_deck(deck)

    def __len__(self):
        return len(self.cards)


class NoCardsException(Exception):
    """Exception should be raised when list of cards is empty, and you try to take one more card"""
