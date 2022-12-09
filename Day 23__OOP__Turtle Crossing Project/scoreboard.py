from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-220, 260)
        self.level = 0
        self.print_score()

    def print_score(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def add_score(self):
        self.level += 1
        self.clear()
        self.print_score()

    def game_over(self):
        self.clear()
        self.write(f"Game Over", align="center", font=FONT)
