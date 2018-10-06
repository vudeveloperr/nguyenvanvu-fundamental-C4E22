
# Rule : (x+2)*2
quiz = {
    'sequencenumber' : [8 , 20 , 44, 92 ],
    'right' : 188 
}
print(" S E Q U E N C E  N U M B E R ")
print(*quiz['sequencenumber'], sep=", ")
print("------- F I N D  T H E  N E X T  N U M B E R -------   ")
print("good luck!!")


while True :
    number = int(input("your number : "))
    if number == quiz['right']:   
        print("188 is true answer Congratulation !!")
        break          
    print(number ,"is wrong answer !")
    print("let s' continue ")
  
    

