from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.penup()
        self.move()

    def move(self):
        self.goto(
            random.randint(-270, 271),
            random.randint(-270, 271)
        )