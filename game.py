"""Black Jack game module"""
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

    def draw_cards(self, deck: Deck, number_of_cards: int) -> None:
        """Draw a number of cards from deck to player hand"""

        self.hand.add_cards_from_deck(deck, number_of_cards)

    def update_hand_strength(self):
        """Update and return strength of player hand"""
        # if len(self.hand) == 2:
        #     if all([card in (CardValue.JACK, CardValue.QUEEN, CardValue.KING)] for card in self.hand.cards):
        #         self.hand_strength = 21
        #         return self.hand_strength

        # cards_values = [card.value.value for card in self.hand.cards]
        for card in self.hand.cards:
            self.hand_strength += Player.get_card_strength(card, self.hand)
        return self.hand_strength

    def __str__(self):
        player_str = [self.name, str(self.hand), f'siła: {self.hand_strength}']
        return '\n'.join(player_str)

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

    def start(self):
        """Start new game"""
        self.player.draw_cards(self.deck, 2)
        self.player.update_hand_strength()
        self.croupier.draw_cards(self.deck, 2)
        self.croupier.update_hand_strength()
        self.print_players()

        while True:
            if Game.get_player_decision():
                self.croupier.draw_card(self.deck)
                self.player.draw_card(self.deck)
                player_str = self.player.update_hand_strength()
                self.print_players()
                if player_str > 21:
                    raise Exception('Przegrałeś')
            else:
                if self.player.update_hand_strength() < self.croupier.update_hand_strength():
                    raise Exception('Przegrałeś')
                raise Exception('Wygrałeś')

    def print_players(self):
        """print nice players cards"""
        croupier_lines = str(self.croupier).split('\n')
        player_lines = str(self.player).split('\n')

        max_croupier_line_len = max([len(x) for x in croupier_lines])
        croupier_lines = [x.ljust(max_croupier_line_len + 5, ' ') for x in croupier_lines]

        players_lines = [''.join(x) for x in zip(croupier_lines, player_lines)]
        print('\n'.join(players_lines))

    @staticmethod
    def get_player_decision():
        """Ask player if he wants fold or draw next card"""
        return input('Czy grasz dalej? ') in ('t', 'T')
