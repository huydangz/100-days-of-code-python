from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("yellow")
        self.penup()
        self.goto(0, -280)
        self.x_move = -10
        self.y_move = 10

    def move(self):
        self.goto(
            self.xcor() + self.x_move,
            self.ycor() + self.y_move
        )

    def is_hit_paddle(self, paddle):
        return self.xcor() == paddle.turtles[0].xcor() and (self.ycor() - paddle.turtles[0].ycor()) * (self.ycor() - paddle.turtles[-1].ycor()) <= 0

    def is_miss_paddle(self, paddle):
        return self.xcor() == paddle.turtles[0].xcor() and (self.ycor() - paddle.turtles[0].ycor()) * (self.ycor() - paddle.turtles[-1].ycor()) > 0

    def is_hit_upside_downside(self):
        return self.ycor() == 280 or self.ycor() == -280

    def change_direction_paddle(self):
        self.x_move *= -1

    def change_direction_upside_downside(self):
        self.y_move *= -1

    def throw_again(self, paddle):
        self.goto(0, -280)
        self.x_move *= -1
