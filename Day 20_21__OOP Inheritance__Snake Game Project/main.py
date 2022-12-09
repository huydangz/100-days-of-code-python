from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from boundary import Boundary
import time

screen = Screen()
screen.setup(600, 600)
screen.title("Snake game")
screen.bgcolor('black')
screen.tracer(0)

boundary = Boundary()
snake = Snake(20)
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.is_hit_food(food):
        food.move()
        snake.grow()
        scoreboard.add_score()

    if snake.is_hit_wall() or snake.is_hit_tail():
        game_over = True
        scoreboard.game_over()

screen.exitonclick()



