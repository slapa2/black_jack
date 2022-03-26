"""main module use it to start the game"""
from black_jack.game import Game


def main():
    """main function"""
    game = Game(1)
    game.start_game()


if __name__ == '__main__':
    main()
