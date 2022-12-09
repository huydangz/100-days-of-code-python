import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = MOVE_INCREMENT

    def create_car(self):
        t = Turtle()
        t.shape("square")
        t.shapesize(stretch_wid=0.5, stretch_len=1)
        t.color(random.choice(COLORS))
        t.penup()
        y = (random.randint(-210, 250) // 30) * 30
        t.goto(300, y)
        t.setheading(180)
        self.cars.append(t)

    def move_cars(self):
        for t in self.cars:
            t.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

