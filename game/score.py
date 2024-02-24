from models import Player


class PlayerRecord:
    def __init__(self, player_name, player_score, player_mode) -> None:
        self.name: str = player_name
        self.score: int = player_score
        self.mode: str = player_mode

    def __gt__(self, other) -> bool:
        return self.score > other.score

    def __str__(self):
        return f"Name: {self.name} you're score is {self.score} on mode {self.mode}"

    def __eq__(self, other):
        return self.name == other.name and self.mode == other.mode

class GameRecord:
    def __init__(self):
        self.records: list[PlayerRecord] = []

    def add_record(self, player_score: PlayerRecord):
        for existing_record in self.records:
            if existing_record == player_score:
                return max(existing_record, player_score)
        self.records.append(player_score)

    def prepare_records
class ScoreHandler:
    raise NotImplementedError
