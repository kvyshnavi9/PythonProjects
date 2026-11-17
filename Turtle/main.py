import turtle
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
turtle.color("red")
for _ in range(15):
    timmy.forward(10)
    timmy.pencolor("brown")
    timmy.forward(10)

screen = Screen()
screen.exitonclick()