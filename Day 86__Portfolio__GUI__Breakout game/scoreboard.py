from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 350)
        self.write(f"SCORE:{self.score}", align="center", font=("Courier", 30, "bold"))
        self.goto(180, 350)
        self.write(f"LIVES:{self.lives}", align="center", font=("Courier", 30, "bold"))

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_lives(self):
        self.lives -= 1
        self.update_scoreboard()

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 30, "bold"))
