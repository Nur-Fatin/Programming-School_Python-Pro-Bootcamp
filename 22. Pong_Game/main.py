"""Build Pong game -
a ball bouncing across the table and hit the wall
2 players each control a paddle
if one player missed the ball, the other player score a point

what needs to be done:
set up the screen
create 2 paddles , controlled with keystrokes
create a ball at the centre & move the ball across the table
detect collision with wall and bounce
detect the ball collision with the paddle
detect when paddle misses the ball
create a scoreboard - track score
"""
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Detect when the  ball misses the R paddle
    if ball.xcor() > 360:
        ball.restart()
        scoreboard.l_point()
    # Detect when the  ball misses the R paddle
    elif ball.xcor() < -360:
        ball.restart()
        scoreboard.r_point()













screen.exitonclick()
