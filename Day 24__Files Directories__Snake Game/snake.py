from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

SIZE = 20


class Snake:
    def __init__(self):
        self.turtles = []
        for _ in range(0, SIZE):
            t = Turtle(shape="square")
            t.shapesize(0.5, 0.5)
            t.color("blue")
            t.penup()
            t.speed("fastest")
            self.turtles.append(t)

    def move(self):
        for n in range(len(self.turtles) - 1, 0, -1):
            self.turtles[n].goto(self.turtles[n - 1].position())
        self.turtles[0].forward(10)

    def up(self):
        if self.turtles[0].heading() != DOWN:
            self.turtles[0].setheading(UP)

    def down(self):
        if self.turtles[0].heading() != UP:
            self.turtles[0].setheading(DOWN)

    def left(self):
        if self.turtles[0].heading() != RIGHT:
            self.turtles[0].setheading(LEFT)

    def right(self):
        if self.turtles[0].heading() != LEFT:
            self.turtles[0].setheading(RIGHT)

    def grow(self):
        t = Turtle(shape="square")
        t.shapesize(0.5, 0.5)
        t.color("blue")
        t.penup()
        t.speed("fastest")
        t.goto(self.turtles[-1].position())
        self.turtles.append(t)

    def is_hit_wall(self):
        return self.turtles[0].xcor() > 270 or self.turtles[0].xcor() < -270 or self.turtles[0].ycor() > 270 or self.turtles[0].ycor() < -270

    def is_hit_tail(self):
        for t in self.turtles[1:]:
            if self.turtles[0].xcor() == t.xcor() and self.turtles[0].ycor() == t.ycor():
                return True

    def is_hit_food(self, food):
        return self.turtles[0].distance(food) < 10

    def reset(self):
        for t in self.turtles:
            t.hideturtle()
        self.turtles.clear()
        self.__init__()
