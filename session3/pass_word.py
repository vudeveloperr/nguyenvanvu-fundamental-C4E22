while True:
    pwd = input("enter your password :  ")
    if len(pwd) <8:
        print("Not long enough")
    elif pwd.isdigit():
        print(" not contain only digits")
    elif pwd.isupper():
        print("Must contain lowercase letters")
    elif pwd.islower():
        print("Must contain uppercase letters")        
    else:
        print("OK")
        break    




 #   if  len(password) >=8:
  #      print("ok")
   #     if not password.isdigit():
    #        print("ok")
     #       break
      #  else:
       #     print("must not containi only digits")
  #  else :
   #     print("not long")    
    
        
