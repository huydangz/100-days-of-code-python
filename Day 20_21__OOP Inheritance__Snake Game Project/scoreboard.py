from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.write(f"Score: {self.score}", False, "center")

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, "center")

    def game_over(self):
        self.home()
        self.write("GAME OVER", False, "center")