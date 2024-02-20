from settings import PLAYER_LIVES
from exceptions import InvalidInput
from exceptions import incorrect_input


class Player:
    def __init__(self):
        self.name: str = input("Enter your name")
        self.lives: int = PLAYER_LIVES
        self.score: int = 0

    def select_attack(self):
        while True:
            user_input = input("Input enter 1, 2, 3: ")
            try:
                incorrect_input(user_input)
                break
            except InvalidInput:
                print("Please input numbers: 1, 2, 3")
                continue

play = Player()
play.select_attack()

# class Enemy:
