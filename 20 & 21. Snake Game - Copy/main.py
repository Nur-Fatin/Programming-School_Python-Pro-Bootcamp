from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    # Detect collision with Food
    if snake.head.distance(food) < 15:
        score.add_score()
        snake.add_part(snake.snake[-1].position())
        food.recreate()

    # Detect collision with Wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()

    # Detect collision with tail
    # When game over, reset the score and snake
    for part in snake.snake[3:]:
        if part.distance(snake.head) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
