from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.print_score()

    def print_score(self):
        self.goto(-50, 270)
        self.write(f"{self.score_1}", align="center", font=("Courier", 22, "bold"))
        self.goto(50, 270)
        self.write(f"{self.score_2}", align="center", font=("Courier", 22, "bold"))

    def update_score(self, paddle):
        if paddle.side == "left":
            self.score_2 += 1
        elif paddle.side == "right":
            self.score_1 += 1
        self.clear()
        self.print_score()
