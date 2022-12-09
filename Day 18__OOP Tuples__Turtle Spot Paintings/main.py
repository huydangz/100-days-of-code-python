import random
import turtle
from turtle import Turtle, Screen
import colorgram

# extract image to 13 most-used colors
colors = colorgram.extract('image.jpg', 13)

turtle.colormode(255)
t = Turtle()
t.penup()
t.speed('fastest')
t.setheading(225)
t.forward(250)
t.setheading(0)

side = 10
for _ in range(1, side + 1):
    for _ in range(1, side + 1):
        rgb = random.choice(colors).rgb
        t.dot(20, rgb)
        t.forward(40)
    t.setheading(90)
    t.forward(40)
    t.setheading(180)
    t.forward(40*side)
    t.setheading(0)

screen = Screen()
screen.exitonclick()
