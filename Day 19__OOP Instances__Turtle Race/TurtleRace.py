from turtle import Turtle
import random

rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
number_of_turtle = 7
distance = 20


class TurtleRace:
    def __init__(self):
        self.turtles = {}
        for n in range(0, number_of_turtle):
            t = Turtle()
            t.shape("turtle")
            t.color(rainbow_colors[n])
            t.penup()
            t.speed("fastest")
            y = (1 - number_of_turtle + 2*n) * distance
            t.setposition(-500, y)
            t.setheading(0)
            self.turtles[rainbow_colors[n]] = t

    def step(self):
        for color in rainbow_colors:
            self.turtles[color].forward(random.randint(5, 15))

    def winner_color(self):
        for color in rainbow_colors:
            if self.turtles[color].xcor() >= 500:
                return color
        return ""

    def race(self):
        while self.winner_color() == "":
            self.step()
