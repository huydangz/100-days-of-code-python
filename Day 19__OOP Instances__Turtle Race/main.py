from turtle import Turtle, Screen
from TurtleRace import TurtleRace

screen = Screen()
screen.setup(1070, 400)
choice = screen.textinput("Make your bet", "Who will win the race? Choose a color:")

turtle_race = TurtleRace()
turtle_race.race()
winner_color = turtle_race.winner_color()

if choice != winner_color:
    print(f"You lose. The {winner_color} turtle is the winner.")
else:
    print("You win.")

screen.exitonclick()

