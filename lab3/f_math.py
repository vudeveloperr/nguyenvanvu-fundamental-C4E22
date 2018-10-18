from random import randint

x = randint(0,10)
y = randint(0,10)
s = randint(0,20)
error = randint(-1,1)
p = x+ y + error
print("{0} + {1} = {2}".format(x,y,s))

user_answer = input("(Y/N)?").upper()
if error == 0:
    if user_answer == "Y":
        print("yeah")
    else:
        print("you are wrong")    
else:
    if user_answer == "y":
        print("you are wrong") 
    else:
        print("yeah")    









