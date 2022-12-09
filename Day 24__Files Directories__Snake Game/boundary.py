from turtle import Turtle

class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(-280, -280)
        self.color("white")
        for _ in range(0, 4):
            self.forward(560)
            self.left(90)


