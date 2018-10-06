quiz = {
    'answer':[24 , 22 , 26 , 28],
    'right': 2
}
print("if x = 8 , then what is the value of 2*(x+3)")

print("good luck!!")


act = 1
for item in quiz['answer']:
    print(act,". " ,item)
    act += 1

while True :
    act = int(input("your number : "))
    if act == quiz['right']:   
        print('right'," is true answer Congratulation !!")
        break          
    print(act ,"is wrong answer !")
    print("let s' continue ")