from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(1, 5)
        self.color('blue')
        self.setpos(0, -300)

    def left(self):
        self.goto(
            self.xcor() - 20,
            self.ycor()
        )

    def right(self):
        self.goto(
            self.xcor() + 20,
            self.ycor()
        )
