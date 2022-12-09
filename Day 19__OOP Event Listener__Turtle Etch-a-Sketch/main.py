from turtle import Turtle, Screen

t = Turtle()

def move_forwards():
    t.forward(100)

def move_backwards():
    t.backward(100)

def clockwise():
    t.right(20)

def counter_clockwise():
    t.left(20)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen = Screen()
screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear, "c")
screen.exitonclick()
