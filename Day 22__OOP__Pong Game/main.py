from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)

paddle_1 = Paddle('left')
paddle_2 = Paddle('right')
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(paddle_1.up, "q")
screen.onkey(paddle_1.down, "a")
screen.onkey(paddle_2.up, "p")
screen.onkey(paddle_2.down, "l")

game_over = False
sleep = 0.101
while not game_over:
    screen.update()
    time.sleep(sleep)

    ball.move()
    paddle_1.move()
    paddle_2.move()

    for paddle in [paddle_1, paddle_2]:
        if ball.is_hit_paddle(paddle):
            ball.change_direction_paddle()
            sleep -= 0.01

    if ball.is_hit_upside_downside():
        ball.change_direction_upside_downside()

    for paddle in [paddle_1, paddle_2]:
        if ball.is_miss_paddle(paddle):
            scoreboard.update_score(paddle)
            ball.throw_again(paddle)
            sleep = 0.1

screen.exitonclick()
