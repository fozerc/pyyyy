from game.models import Enemy
from game.models import Player
from game.settings import ATTACK_PAIRS_OUTCOME, HARD_MODE_MULTIPLIER
from game.exceptions import EnemyDown
from game.exceptions import GameOver
from game.score import ScoreHandler, GameRecord, PlayerRecord


class Game:
    def __init__(self, player_object: Player, game_mode: str):
        """
        Creates players and enemy attributes.
        """
        self.player = player_object
        self.level = 1
        self.mode = game_mode
        self.enemy = Enemy(self.level, self.mode)
        self.score_handler = ScoreHandler()

    def create_enemy(self, enemy_level: int, game_mode: str) -> None:
        """
        Creates a new enemy.
        """
        self.enemy = Enemy(enemy_level, game_mode)

    def fight(self, player_attack: str, enemy_attack: str) -> int:
        """
        Returns result of players and enemy fight from const.
        """
        return ATTACK_PAIRS_OUTCOME.get((player_attack, enemy_attack))

    def handle_fight_result(self, match_result: int) -> None:
        """
        Decreases HP's based on match result.
        """
        if match_result == 1:
            self.enemy.decrease_lives()
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
                self.save_player_score()
                break
            except EnemyDown:
                self.player.add_score()
                self.save_player_score()
                self.create_enemy(self.enemy.level + 1, self.mode)
                print(f"Enemy is dead, you got +5 points, "
                      f"now you're score is - {self.player.score}. "
                      f"Here is a new enemy with higher lvl {self.enemy.level}")

    def save_player_score(self):
        player_record = PlayerRecord(self.player.name, self.player.score, self.mode)
        self.score_handler.game_record.add_record(player_record)
        self.score_handler.save()
