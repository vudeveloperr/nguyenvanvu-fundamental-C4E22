from turtle import *
def draw_square(length,linecolor):
    shape("turtle")
    for i in range(4):
        color(linecolor)
        forward(length)
        left(90)
      
draw_square(100,"red")
mainloop()