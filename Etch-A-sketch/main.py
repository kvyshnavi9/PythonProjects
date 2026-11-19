from turtle import Turtle, Screen

tim= Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def clockwise():
    tim.left(10)
    tim.forward(10)

def anti_clockwise():
    tim.right(10)
    tim.forward(10)

def clear():
    tim.clear()

screen.listen()
screen.onkey(key = "w" ,fun = move_forward) #fn as an input to another fn - no need of paranthesis
screen.onkey(key = "s" ,fun = move_backward)
screen.onkey(key = "a" ,fun = clockwise)
screen.onkey(key = "d" ,fun = anti_clockwise)
screen.onkey(key = "c" ,fun = clear)
screen.exitonclick()