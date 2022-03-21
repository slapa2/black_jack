"""Black Jack player module"""

from math import fabs
from cards import Hand, Deck, Card, CardValue


class Player:
    """Player class"""

    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.hand_strength = 0

    def draw_card(self, deck: Deck) -> None:
        """Add card from deck to player hand"""
        self.hand.add_card_from_deck(deck)
        self.update_hand_strength()

    def draw_cards(self, deck: Deck, number_of_cards: int) -> None:
        """Draw a number of cards from deck to player hand"""
        self.hand.add_cards_from_deck(deck, number_of_cards)
        self.update_hand_strength()

    def update_hand_strength(self):
        """recount strength of hand"""
        self.hand_strength = 0
        for card in self.hand.cards:
            self.hand_strength += Player.get_card_strength(card, self.hand)
        return self.hand_strength

    @staticmethod
    def get_card_strength(card: Card, hand: Hand) -> int:
        """Return strength of a card"""
        if card.value.value.isdigit():
            strength = int(card.value.value)
        elif card.value == CardValue.ACE:
            if len(hand) > 3:
                strength = 1
            else:
                strength = 11
        else:
            strength = 10
        return strength

    def get_player_info(self):
        """return tuple with player infos"""
        return (
            self.name,
            ', '.join([str(x) for x in self.hand.cards]),
            f'siła: {self.hand_strength}',
        )

    def get_hidden_player_info(self):
        """return tuple with hidden cards"""
        return (
            self.name,
            f'{"[], " * (len(self.hand) - 1)} {str(self.hand.cards[0])}',
            'siła: ?',
        )

    def get_end_round_points(self):
        """return absolut difference between player hand and 21 points"""
        return fabs(21 - self.hand_strength)
