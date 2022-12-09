from turtle import Turtle

FONT = ("Courier", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score}. High score: {self.high_score}", align="center", font=FONT)

    def add_score(self):
        self.score += 1
        self.print_score()

    def game_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")
        self.score = 0
        self.print_score()
