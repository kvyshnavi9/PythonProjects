import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500,400)
bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter the color")

colors = ["orange","yellow","red","green","pink","violet"]

turtles =[]
def turtle_race(colors):
    for n, color in enumerate(colors):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.goto(x=-230, y=100-(n*50))
        turtles.append(new_turtle)

turtle_race(colors)

if bet:
    is_race_on = True
else:
    is_race_on = False
    print("Please enter a bet!")

while is_race_on:
    for turle in turtles:
        if turle.xcor() > 230:
            is_race_on = False
            winning_color = turle.pencolor()

            if winning_color == bet.lower():
                print(f"You won the race! {winning_color}")
            else:
                print(f"You lost the race! {winning_color}")

            break

        rand_distance = random.randint(0, 10)
        turle.forward(rand_distance)





screen.exitonclick()