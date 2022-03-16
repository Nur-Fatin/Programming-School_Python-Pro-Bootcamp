import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("The Turtle Crossing Game")

turtle = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=turtle.move, key="Up")

iteration = 0
cars = []
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    iteration += 1
    if iteration % 6 == 0:
        car = CarManager()
        cars.append(car)

    for car in cars:
        car.car_move()

        # Detect collision with the car
        if turtle.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect when turtle has reached the finish line
    if turtle.ycor() > 280:
        turtle.start()
        scoreboard.level_up()
        for car in cars:
            car.increase_speed()

screen.exitonclick()
