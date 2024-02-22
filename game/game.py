from models import Player, Enemy
from settings import ATTACK_PAIRS_OUTCOME
from settings import WIN, DRAW, LOSE
from exceptions import EnemyDown
from exceptions import GameOver

class Game:
    def __init__(self):
        """
        creates players and enemy attributes
        """
        self.player = Player()
        self.enemy = Enemy()
        # self.mode

    def create_enemy(self, level: int) -> None:
        """
        creates a new enemy
        :return None:
        """
        self.enemy = Enemy()

    def fight(self, player_attack: str, enemy_attack: str) -> int:
        """
        returns result of players and enemy fight from const
        :param player_attack: players attack
        :param enemy_attack: enemy attack
        :return: int
        """
        return ATTACK_PAIRS_OUTCOME.get((player_attack, enemy_attack))

    def handle_fight_result(self, match_result: int) -> None:
        """
        decrease hp's bases on match result
        :param match_result: teh result of fight
        :return: None
        """
        if match_result == 1:
            self.enemy.decrease_lives()
            print("win")
        elif match_result == -1:
            self.player.decrease_lives()
        elif match_result == 0:
            print("Draw!")

    def play(self):
        while True:
            try:
                self.handle_fight_result(
                    self.fight(
                        self.player.select_attack(),
                        self.enemy.select_attack()))
            except GameOver:
                print("You're dead, try to play again")
                break
            except EnemyDown:
                print("Enemy is dead, ready to new fight?")


# def fight(player_attack, enemy_attack):
#     for player_attack in ATTACK_PAIRS_OUTCOME:
#         print(player_attack)
# fight()

# player_attack = Player()
# enemy_attack = Enemy()
# play = player_attack.select_attack()
# enem = enemy_attack.select_attack()
#
igra = Game()
igra.play()
