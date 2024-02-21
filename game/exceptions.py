from settings import ALLOWED_ATTACKS

class InvalidInput(Exception):
    pass

def incorrect_input(input_int):
    if input_int not in ALLOWED_ATTACKS:
        raise InvalidInput("Incorrect input")


class GameOver(Exception):
    pass

def player_dead(player_lives):
    if player_lives == 0:
        raise GameOver("You're dead, try to play again!")


class EnemyDown(Exception):
    pass

def enemy_dead(enemy_lives):
    if enemy_lives == 0:
        raise EnemyDown("Enemy is dead, you're win!")