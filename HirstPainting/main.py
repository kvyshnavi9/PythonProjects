import colorgram
import turtle as t
import random

colors = colorgram.extract('image.jpg',15)

# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g=  color.rgb.g
#     b= color.rgb.b
#
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(226, 225, 222), (206, 78, 6), (226, 219, 222), (8, 12, 48), (105, 192, 177), (228, 39, 65), (171, 192, 6), (216, 226, 219), (186, 134, 121), (133, 157, 187), (63, 105, 125), (175, 2, 119), (59, 171, 4), (24, 84, 64), (218, 221, 226)]

t.colormode(255)
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(300)
t.setheading(0)

no_of_dots = 100

def dot_painting():
    t.speed("fastest")
    for n in range(1,no_of_dots+1):
        t.dot(20, random.choice(color_list))
        t.forward(50)

        if n % 10 == 0:
            t.setheading(90)
            t.forward(50)
            t.setheading(180)
            t.forward(500)
            t.setheading(0)

dot_painting()

screen = t.Screen()
screen.exitonclick()
