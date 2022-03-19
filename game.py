"""Black Jack game module"""
import os
from math import fabs
from cards import Hand, Deck, Card, CardValue, CardsList


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
        """recount strength of heand"""
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


class Game:
    """Main Black Jack Game class"""

    def __init__(self, deck_number: int) -> None:
        self.deck = Deck()
        for _ in range(deck_number):
            self.deck.add_standard_52_cards_deck()
        self.deck.shuffle()

        self.croupier = Player('Croupier')
        self.player = Player('Player')

    def start_game(self):
        """start a new game"""
        while True:
            try:
                self.start_round()
            except Exception as ex:
                self.player.hand.remove_cards()
                self.croupier.hand.remove_cards()
                print(ex)
                input()

    def start_round(self):
        """Start new round"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\nNEW ROUND')
        self.deal_the_cards()
        while Game.get_player_decision():
            os.system('cls' if os.name == 'nt' else 'clear')
            self.play_round()

        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_players(show_all_croupier_cards=True)
        player_points = fabs(21 - self.player.hand_strength)
        croupier_points = fabs(21 - self.croupier.hand_strength)
        if croupier_points < player_points:
            raise Exception('You lost!')
        raise Exception('You win!')

    def deal_the_cards(self):
        """deal cards in new round"""
        self.player.draw_cards(self.deck, 2)
        self.croupier.draw_cards(self.deck, 2)
        self.print_players()
        self.check_if_black_jack()

    def play_round(self):
        """play round"""
        self.croupier.draw_card(self.deck)
        self.player.draw_card(self.deck)
        self.print_players()
        if self.player.hand_strength > 21:
            raise Exception('Przegrałeś!')

    @staticmethod
    def _get_player_info(plyer):
        """returns tuple with player info"""
        return (
            plyer.name,
            ', '.join([str(x) for x in plyer.hand.cards]),
            f'siła: {plyer.hand_strength}',
        )

    def print_players(self, show_all_croupier_cards=False):
        """print nice players cards"""

        if show_all_croupier_cards:
            croupier_info = self._get_player_info(self.croupier)
        else:
            croupier_info = (
                self.croupier.name,
                f'{"[], " * (len(self.croupier.hand) - 1)} {str(self.croupier.hand.cards[-1])}',
                'siła: ?',
            )
        player_info = self._get_player_info(self.player)

        max_croupier_line_len = max([len(x) for x in croupier_info])
        croupier_info = [x.ljust(max_croupier_line_len + 5, ' ') for x in croupier_info]

        players_lines = [''.join(x) for x in zip(croupier_info, player_info)]
        print('\n'.join(players_lines))

    @staticmethod
    def get_player_decision():
        """Ask player if he wants fold or draw next card"""
        return input('[H]it or [S]tand? ') in ('H', 'h', 'Hit', 'hit', 'HIT')

    def check_if_black_jack(self) -> None:
        """raise exception if player has Black Jacki after 2 first Cards"""
        if len(self.player.hand) != 2:
            raise Exception('Possible only for two on hand')
        ten_values_cards = {CardValue.KING, CardValue.QUEEN, CardValue.JACK, CardValue.TEN}
        player_cards_values = {x.value for x in self.player.hand.cards}

        if (CardValue.ACE in player_cards_values and
                player_cards_values.intersection(ten_values_cards)):
            raise Exception('-> BLACK JACK <- You win!')
