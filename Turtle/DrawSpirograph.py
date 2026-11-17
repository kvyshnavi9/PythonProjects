import random
import turtle as t

tim = t.Turtle()
t.colormode(255)
def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b = random.randint(0,255)
    color =  (r,g,b)
    return color

tim.speed("fastest")
# tim.color(random_color())
# tim.circle(100)
# current_heading = tim.heading()
# tim.setheading(current_heading+10)
# tim.circle(100)

def spirograph(size_of_gap):
    for n in range(int(360/size_of_gap)):
        tim.color(random_color())
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)
        tim.circle(100)

spirograph(5)
