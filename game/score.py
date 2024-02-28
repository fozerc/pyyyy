from game.settings import MAX_RECORDS_NUMBER, SCORE_FILE


class PlayerRecord:
    """
    contains a record of one player and uses magic method's to compare with others players
    """
    def __init__(self, player_name, player_score, player_mode) -> None:
        self.name: str = player_name
        self.score: int = player_score
        self.mode: str = player_mode

    def __gt__(self, other) -> bool:
        return self.score > other.score

    def __str__(self) -> str:
        return f"Name: {self.name} you're score is {self.score} on mode {self.mode}"

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.mode == other.mode


class GameRecord:
    """
    contains a list with record of all players
    """
    def __init__(self):
        self.records: list[PlayerRecord] = []

    def add_record(self, player_score: PlayerRecord):
        for existing_record in self.records:
            if existing_record == player_score:
                return max(existing_record, player_score)
        self.records.append(player_score)

    def prepare_records(self):
        self.records.sort()
        self.records = self.records[:MAX_RECORDS_NUMBER]


class ScoreHandler:
    """
    class for processing scores.
    displays all scores in console and writes every score in txt file
    """
    def __init__(self):
        self.game_record = GameRecord()
        self.file_name = SCORE_FILE
        self.read()

    def read(self):
        opened_file = open(self.file_name, 'r')
        for line in opened_file:
            player_data = line.split(",")
            self.game_record.add_record(PlayerRecord(player_data[0], player_data[1], player_data[2]))
        opened_file.close()

    def save(self):
        GameRecord().prepare_records()
        with open(self.file_name, "w") as file:
            for record in self.game_record.records:
                file.write(f"{record.name}, {record.mode}, {record.score}\n")

    def display(self):
        for display_record in open(self.file_name):
            print(display_record)
