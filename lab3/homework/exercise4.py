from turtle import *

def draw_square(length,linecolor):
    speed(0)
    shape("turtle")
    for i in range(4):
        color(linecolor)
        forward(length)
        left(90)

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

draw_square(100,"red")
mainloop()