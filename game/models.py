from settings import PLAYER_LIVES, POINTS_FOR_KILLING, ALLOWED_ATTACKS, HARD_MODE_MULTIPLIER, MODES
from exceptions import InvalidInput
from exceptions import incorrect_input
from exceptions import GameOver
from exceptions import player_dead
from exceptions import EnemyDown
from exceptions import enemy_dead
from random import randint

class Player:
    def __init__(self):
        """
        Create players attributes
        """
        self.name: str = input("Enter your name to start game: ")
        self.lives: int = PLAYER_LIVES
        self.score: int = 0

    def select_attack(self) -> str:
        """
        Creates an infinite loop asking the player for his turn
        :return string:
        """
        while True:
            user_input = input("Choose you're weapon 1 - PAPER, 2 - STONE, 3 - SCISSORS: ")
            try:
                incorrect_input(user_input)
                return ALLOWED_ATTACKS.get(user_input)
            except InvalidInput:
                print("Please input numbers: 1, 2, 3")
                continue

    def decrease_lives(self) -> None:
        """
        Decrease players hp and when player's hp 0 raise GameOver
        :return None:
        """
        self.lives -= 1
        print("You got -1 hp")
        try:
            player_dead(self.lives)
        except GameOver:
            raise GameOver

    def add_score(self):
        self.score += POINTS_FOR_KILLING


class Enemy:
    def __init__(self, enemy_level: int, game_mode: str):
        """
        Creates enemy attributes
        """
        self.level: int = enemy_level
        if game_mode == '1' in MODES:
            self.lives: int = enemy_level + 1
        elif game_mode == '2' in MODES:
            self.lives: int == enemy_level + HARD_MODE_MULTIPLIER

    def select_attack(self) -> str:
        """
        Makes random attack for bot
        :return str:
        """
        random_attack = str(randint(1, 3))
        return ALLOWED_ATTACKS.get(random_attack)

    def decrease_lives(self) -> None:
        """
        Decrease enemy hp and when enemy's hp 0 raise GameOver
        :return: None
        """
        self.lives -= 1
        print("Enemy got -1 hp")
        try:
            enemy_dead(self.lives)
        except EnemyDown:
            raise EnemyDown
