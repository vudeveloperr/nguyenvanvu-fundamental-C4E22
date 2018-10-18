from random import randint , choice
from calc import eval

def generate_quiz():
    x = randint(0,10)
    y = randint(1,10)
    s = randint(-5,100)
    op = choice(["+" , "-" , "/" , "*"])
    #error = randint(-1,1)

    r = eval(x,y,op)

    return [x,y,op,s,r]

x, y, op,s,r = generate_quiz()

# r = eval(x,y,op)
#print(x,op,y,"=",r)
print("{0} {3} {1} = {2}".format(x,y,s,op).upper())

# single entitys
user_answer = input("(Y/N)?")
if r == s:
    if user_answer == "y":
        print("right")
    else:
        print("wrong")    

else:
    if user_answer == "y":
        print("wrong") 
    else:
        print("right")        


