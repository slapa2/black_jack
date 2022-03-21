"""Black Jack game module"""

from cards import Deck, CardValue, NoCardsException
from player import Player
from game_interface import Interface


class Game:
    """Main Black Jack Game class"""

    def __init__(self, deck_number: int) -> None:
        self.deck = Deck()
        for _ in range(deck_number):
            self.deck.add_standard_52_cards_deck()
        self.deck.shuffle()

        self.dealer = Player('Dealer')
        self.player = Player('Player')

    def start_game(self) -> None:
        """
        start a new game.
        game will end when there will be no cards in deck
        """
        while True:
            try:
                self.start_round()
            except DealerWonRoundEndException as exception:
                print(exception)
            except PlayerWonRoundEndException as exception:
                print(exception)
            except NoCardsException as exception:
                print("Pusta talia kart - koniec gry")
                break
            finally:
                Interface.wait_for_confirmation()

    def start_round(self) -> None:
        """
        Start new round.
        Round will end when dealer or player will win teh round
        """
        Interface.new_round_info()
        self.player.hand.remove_cards()
        self.dealer.hand.remove_cards()
        self.deal_the_cards()
        self.play_round()

    def play_round(self) -> None:
        """
        play round
        player and dealer draws card until
        player hand strength will be higher than 21 or player will stand
        """
        while Interface.get_player_decision():
            self.dealer.draw_card(self.deck)
            self.player.draw_card(self.deck)
            Interface.print_players(self)
            if self.player.hand_strength > 21:
                raise DealerWonRoundEndException('Przegrałeś! przekroczyłeś 21 pkt.')

        Interface.print_players(self, show_all_croupier_cards=True)
        if self.dealer.get_end_round_points() < self.player.get_end_round_points():
            raise DealerWonRoundEndException('You lost!')
        raise PlayerWonRoundEndException('You win!')

    def deal_the_cards(self) -> None:
        """
        Deal cards in new round.
        Player and dealer gets 2 cards fom deck
        """
        self.player.draw_cards(self.deck, 2)
        self.dealer.draw_cards(self.deck, 2)
        Interface.print_players(self)
        self.check_if_black_jack()

    def clear_players_hands(self) -> None:
        """remove cards form players hands"""
        self.player.hand.remove_cards()
        self.dealer.hand.remove_cards()

    def check_if_black_jack(self) -> None:
        """
        Raise exception if player has Black Jack
        (21 points with ase and any figure) after 2 first Cards
        """
        if len(self.player.hand) != 2:
            raise Exception('Possible only for two on hand')
        ten_values_cards = {CardValue.KING, CardValue.QUEEN, CardValue.JACK, CardValue.TEN}
        player_cards_values = {x.value for x in self.player.hand.cards}

        if (CardValue.ACE in player_cards_values and
                player_cards_values.intersection(ten_values_cards)):
            raise PlayerWonRoundEndException('-> BLACK JACK <- You win!')


class RoundEndException(Exception):
    """Exception that round end with any reason """


class DealerWonRoundEndException(RoundEndException):
    """Exception that Player lost the round"""


class PlayerWonRoundEndException(RoundEndException):
    """Exception that Player won the round"""
