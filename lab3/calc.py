from random import choice
# funcion scope
# def add(x,y):
#     r = x + y
#     return r

# def eval(x,y,op):
#     x = int(input("x = "))
#     y = int(input("y = "))
#     op = choice(["+","-","*","/"])     
#     return r
# print(eval(x,y,op))  

def eval(x,y,op):
    if op == "+":
        i = x + y
        return i
    elif op == "-":
        i = x - y
        return i 
    elif op == "*":
        i = x*y
        return i
    elif op == "/":
        i = x / y
        return i

# a= int(input("a = "))
# b= int(input("b = "))

# t = add(a,b) 
# print(t)  
