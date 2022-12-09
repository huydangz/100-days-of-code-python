from turtle import Turtle

UP = 90
DOWN = 270

SIZE = 7


class Paddle:
    def __init__(self, side):
        self.side = side
        self.turtles = []
        for n in range(0, SIZE):
            t = Turtle(shape="square")
            t.shapesize(0.5, 0.5)
            t.color("blue")
            t.penup()
            if side == "left":
                t.goto(-390, 20 - 10*n)
            elif side == "right":
                t.goto(380, 20 + 10*n)
            t.speed("fastest")
            self.turtles.append(t)
        self.turtles[0].setheading(UP)

    def move(self):
        for n in range(SIZE - 1, 0, -1):
            self.turtles[n].goto(self.turtles[n - 1].position())
        self.turtles[0].forward(10)

        if self.is_hit_wall():
            if self.turtles[0].heading() == UP:
                self.down()
            else:
                self.up()

    def up(self):
        if self.turtles[0].heading() == DOWN:
            self.turtles.reverse()
            self.turtles[0].setheading(UP)

    def down(self):
        if self.turtles[0].heading() == UP:
            self.turtles.reverse()
            self.turtles[0].setheading(DOWN)

    def is_hit_wall(self):
        return self.turtles[0].ycor() == 280 or self.turtles[0].ycor() == -280
