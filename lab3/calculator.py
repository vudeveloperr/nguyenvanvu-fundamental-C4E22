x = int(input("x = "))
y = int(input("y = "))

op = input("op (+ ,-, /, *)")

if op == "+":
    r =  x + y
elif op == "-":
    r = x - y
elif op == "/":
    r = x / y
elif op == "*":
    r = x * y
else:
    print("invalid operators")




