"""
1. create white screen
2. randomly create a bunch of colourful cars moving horizontally continuously. speed up when player move to the next level
3. create a turtle, which the player control, can move forward only
4. create a scoreboard to keep track the current level
5. tell user when the game over
"""

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move, key="Up")

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            is_game_on = False
            scoreboard.game_over()

    # Detect arrival at the finish line
    if player.is_at_finish_line():
        player.restart()
        car_manager.level_up()
        scoreboard.increase_level()




screen.exitonclick()
