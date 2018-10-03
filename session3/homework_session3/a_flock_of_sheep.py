# i'm a shepherd who owns a flock of sheep hi hi

sheeps = [15, 17, 300, 40, 50, 75, 95]
print(*sheeps, sep=", ")
print("\nflock size :" , len(sheeps))   #size of sheep in flock


# find the biggest sheep in flock
highest = max(sheeps)
print("\nnow my biggest sheep has size " ,max(sheeps) ,",let 's shear it")


# shearing
print("\nIndex for biggest sheep in flock  : ", sheeps.index( max(sheeps) ))
p = sheeps.index( max(sheeps) )
sheeps[p] = 8       # shearing
print(*sheeps, sep=", ")

print("--------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------")
print("\n")
#In the following month, EVERY sheep in your flock grow, 
# they have their size increased by 50. Print them out 

for i in range(1,5):
    for index, item in enumerate(sheeps):    
        sheeps[index] += 50           # sheep grow
    print("\nMonth" ,i ,":")    
    print(*sheeps, sep=", ")
    highest = max(sheeps)
    print("now my biggest sheep has size " ,max(sheeps) ,",let 's shear it")    #biggest size sheep
    print("Index for biggest sheep in flock  : ", sheeps.index( max(sheeps)  )) # index biggest
    p = sheeps.index( max(sheeps)  )
    sheeps[p] = 8
    print(*sheeps, sep=", ")    # after shear



# After day by day shearing sheep, i became bored.
# I want to sell my flock to travel the world. 
# In order to have fair trade, 
# I must now calculate the total size of my sheep 
# and then the expected money I can get from my flock before going to the market. 
# Write a program to calculate the total size of my sheep as well as the money I would have

print("--------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------")


for i in range(1,4):
    for index, item in enumerate(sheeps):    
        sheeps[index] += 50
    print("\nMonth" ,i ,":")    
    print(*sheeps, sep=", ")
    highest = max(sheeps)
    if i<=2 :           # before
        print("now my biggest sheep has size " ,max(sheeps) ,",let 's shear it")
        print("Index for biggest sheep in flock  : ", sheeps.index( max(sheeps) ))
        p = sheeps.index( max(sheeps) )
        sheeps[p] = 8
        print(*sheeps, sep=", ")

s = 0
for index, item in enumerate(sheeps):    
    s += sheeps[index]      #sum of size sheeps
print("\nMy flock has size in total : ", s )
print("price of 1 size sheep is 500$ ")
pay = s*500                             # multiplication
print("i would get : ",pay,"$")

print("oh my goddesss ", pay , " i became a Young Millionare !")
print("\n\t yes i'm going to travel the world car hu yeahhh  !!!!!!")



