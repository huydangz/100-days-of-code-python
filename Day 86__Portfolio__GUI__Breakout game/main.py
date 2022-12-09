from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from bricks import Bricks
import time

screen = Screen()
screen.setup(600, 800)
screen.bgcolor('black')
screen.title("Breakout Game")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
scoreboard = ScoreBoard()
bricks = Bricks()

screen.listen()
screen.onkey(paddle.left, 'Left')
screen.onkey(paddle.right, 'Right')

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Hit wall
    if ball.xcor() < -280 or 280 < ball.xcor():
        ball.bounce_x()

    # Hit paddle
    if ball.distance(paddle) < 25 and -300 < ball.ycor():
        ball.bounce_y()

    # Hit bricks
    for brick in bricks.all_bricks:
        if ball.distance(brick) < 25:
            ball.bounce_y()
            brick.hideturtle()
            bricks.all_bricks.remove(brick)
            scoreboard.update_score()

    # Ball drop
    if ball.ycor() < -300:
        ball.reset_position()
        scoreboard.update_lives()
        if scoreboard.lives == 0:
            scoreboard.gameover()
            game_on = False

screen.exitonclick()
