print( "Welcome to our shop, what do you want") 
acss = ["T-Shirt", "Sweater" ]

# read 
input(" ")
print("R welcome to ourshop")
print(*acss, sep=", ")

#create
print(" what do you want (C, R, U, D)? ")   
acss.append(input("C  Enter new item : "))
print(*acss, sep=", ")

# update
print(" what do you want (C, R, U, D)?")
p = int(input("U update position ? "))
acss[p-1] = input("new item : ")
print(*acss, sep=", ")

# delete
print(" what do you want (C, R, U, D)?")
i = int(input("D delete position ?"))
acss.pop(i-1)
print(*acss, sep=", ") 

