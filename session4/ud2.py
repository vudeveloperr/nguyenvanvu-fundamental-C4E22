person = {
    'name': 'quan',
    'age' : 22,
}
print(person)
action = input("you want delete 'D' or update 'U' ? ")

#delete
if action == "D" :
    key = input("what key you delete ?")
    if key in person:
        del person[key]
        print(person)
    else:
        print("not found")    

#update
elif action == "U" :
    key = input("what to update ?")
    if key in person : 
        value = input("what to update : ")
        person[key] = value
        print(person)
    else:
        print("not found")
    
else:
    print("wrong !")