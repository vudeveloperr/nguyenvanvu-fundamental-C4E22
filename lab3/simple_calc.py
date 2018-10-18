from calc import * 

x = int(input("x = "))
y = int(input("y = "))

op = input("op (+ ,-,*, /)")
r = eval(x,y,op)

print(x,op,y,"=",r)
