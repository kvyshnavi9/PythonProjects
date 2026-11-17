import turtle as t

tim = t.Turtle()

def draw_shape(num_side):
    angle = 360/num_side
    for _ in range(num_side):
        tim.forward(100)
        tim.right(angle)

for n in range(3,11):
    draw_shape(n)

