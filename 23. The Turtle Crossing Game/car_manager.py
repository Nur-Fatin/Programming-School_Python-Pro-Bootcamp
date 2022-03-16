from turtle import Turtle
from random import choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_POSITION = [20, 50, 80, 120, 150, 180, 210, 240, -20, -50, -80, -120, -150, -180, -210, -240]


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(choice(COLORS))
        self.speed("fastest")
        self.penup()
        self.goto(x=300, y=choice(Y_POSITION))
        self.x_move = STARTING_MOVE_DISTANCE

    def car_move(self):
        new_x = self.xcor() - self.x_move
        self.goto(new_x, self.ycor())

    def increase_speed(self):
        self.x_move += MOVE_INCREMENT
