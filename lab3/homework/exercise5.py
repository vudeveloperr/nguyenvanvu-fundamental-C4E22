from turtle import *

def draw_star(x,y,length):
    shape("turtle")
    goto(50,100)
    for i in range(5):
        forward(length)
        left(144)
    
    
draw_star(30, 40, 150)
mainloop()
