class Figure:
    place_on_board: tuple = (2, 2)
    color: str = "black"
    def change_color(self):
        if self.color == "black":
            self.color = "white"
        elif self.color == "white":
            self.color = "black"

    def _change_place(self, *args):
        if args[0] > 7 or args[1] > 7:
            return print("ход за пределы доски")
        else:
            self.place_on_board = args
            return print(f"вы походили на клетки {self.place_on_board}")

# class Pawn(Figure):


lox = Figure()
lox._change_place(6, 6)