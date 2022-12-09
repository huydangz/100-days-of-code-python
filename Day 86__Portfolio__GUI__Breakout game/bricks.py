from turtle import Turtle

COLORS = ['green', 'yellow', 'orange']


class Bricks(Turtle):

    def __init__(self):
        super().__init__()
        self.all_bricks = []
        self.hideturtle()
        self.create_bricks()

    def create_bricks(self):
        y = 100
        for color in COLORS:
            for row in range(2):
                x = -265
                y += 25
                while x < 300:
                    brick = Turtle('square')
                    brick.penup()
                    brick.shapesize(1, 3)
                    brick.color(color)
                    brick.goto(x, y)
                    self.all_bricks.append(brick)
                    x += 65

