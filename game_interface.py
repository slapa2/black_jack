"""module with black jack game interface"""

import os
from time import sleep


class Interface:
    """Class with game interface"""

    @staticmethod
    def wait_for_confirmation():
        """wait for any input form user"""
        input('pres any key')

    @staticmethod
    def get_player_decision():
        """Ask player if he wants fold or draw next card"""
        return input('[H]it or [S]tand? ') in ('H', 'h', 'Hit', 'hit', 'HIT')

    @staticmethod
    def print_players(game, show_all_croupier_cards=False):
        """print nice players cards"""

        if show_all_croupier_cards:
            croupier_info = game.dealer.get_player_info()
        else:
            croupier_info = game.dealer.get_hidden_player_info()
        max_croupier_line_len = max([len(x) for x in croupier_info])
        croupier_info = [x.ljust(max_croupier_line_len + 5, ' ') for x in croupier_info]

        player_info = game.player.get_player_info()
        players_lines = [''.join(x) for x in zip(croupier_info, player_info)]

        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n'.join(players_lines))

    @staticmethod
    def new_round_info():
        """Display info than new round started"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print('NEW ROUND')
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
