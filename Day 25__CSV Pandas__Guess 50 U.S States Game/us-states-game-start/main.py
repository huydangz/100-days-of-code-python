from turtle import Turtle, Screen
import pandas

FONT = ("Cambria", 11, "bold")

turtle = Turtle()
screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")


def print_state(state):
    x = int(data[data.state == state].x)
    y = int(data[data.state == state].y)
    t = Turtle()
    t.penup()
    t.hideturtle()
    t.goto(x, y)
    t.write(state, align="center", font=FONT)


def save_states_to_learn():
    states_to_learn = data
    for state in guessed_state:
        states_to_learn = states_to_learn.drop(states_to_learn[states_to_learn.state == state].index)
    states_to_learn.to_csv("states_to_learn.csv", index=False)


guessed_state = []
while len(guessed_state) < 50:
    if len(guessed_state) == 0:
        answer = screen.textinput("Guess US States", prompt="Enter state:").title()
    else:
        answer = screen.textinput(f"{len(guessed_state)}/50 states correct", prompt="Enter another's state:").title()

    if answer not in guessed_state and len(data[data.state == answer]) > 0:
        print_state(answer)
        guessed_state.append(answer)

    if answer == "Exit":
        save_states_to_learn()
        break

# screen.exitonclick()
