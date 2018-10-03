from turtle import *

shape("turtle")

# draw triangular red
for i in range(3): 
    color("red")
    forward(100)
    left(120)

# draw square blue
for i in range(4):
    color("blue")
    forward(100)
    left(90)

# draw pentagonal brown
for i in range(5):
    color("brown")
    forward(100)
    left(72)

# draw hexagonal yellow 
for i in range(6):
    color("yellow")
    forward(100)
    left(60) 

# draw sevengonal grey
for i in range(7):
    color("grey")
    forward(100)
    left(51)       
mainloop()