def is_inside(x , y):
    if x >= 140 & x<=240 & y >= 60 & y <= 260 :
        print("is inside")
    return x,y
    
x = int(input("enter x :"))
y =int(input("enter y :"))
print(is_inside(x, y))
