from game.exceptions import ModeInvalidInput, mode_invalid_input
from game.game import Game
from game.models import Player
from game.score import ScoreHandler


def create_player() -> None:
    """
    create player and start's game
    :return: None
    """
    while True:
        name: str = input(str("Enter your name to start game: "))
        mode: str = input("Choose mode. 1 - Normal. 2 - Hard: ")
        try:
            mode_invalid_input(mode)
            Game(Player(name), mode).play()
            break
        except ModeInvalidInput:
            print("Please write '1' or '2'")
            continue


def play_game() -> None:
    """
    start's game
    :return: None
    """
    create_player()


def show_scores() -> None:
    """
    show's all scores
    :return:
    """
    player_scores = ScoreHandler()
    player_scores.display()


def exit() -> None:
    """
    exit menu
    :return: None
    """
    print("Exit")


def main() -> None:
    """
    game menu
    :return: None
    """
    while True:
        menu_controls = input("1 - Start game. 2 - Check scores. 3 - Exit game: ")
        if menu_controls == '1':
            play_game()
        elif menu_controls == '2':
            show_scores()
        elif menu_controls == '3':
            exit()
        else:
            print("please input 1 - 2 - 3")
            continue


main()

if __name__ == "__main__":
    main()
