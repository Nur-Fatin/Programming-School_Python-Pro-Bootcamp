# How the game work:
# player bet the turtle who will win the race on the popup
# all turtles go to the starting lines, start moving random pace
# the first turtle that arrive at the right end of the screen, won the race game
# user get feedback if their turtle win or not

from turtle import Turtle, Screen
import random

# Set up the screen
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Create 6 turtles and move each turtle to the starting point, the left side of the screen. Line up ready to race
for i in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-230, y=y_position[i])
    all_turtles.append(turtle)

#  Get the turtle to start moving randomly
is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        # Find winning color & tell user if they win or lose
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
