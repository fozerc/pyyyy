from settings import ALLOWED_ATTACKS

class InvalidInput(Exception):
    pass


def incorrect_input(input_int):
    if input_int not in ALLOWED_ATTACKS and \
       input_int not in ALLOWED_ATTACKS and \
       input_int not in ALLOWED_ATTACKS:
       raise InvalidInput("Incorrect input")