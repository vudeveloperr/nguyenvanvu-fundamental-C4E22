person = {
    'name': 'quan',
    'age' : 22,
}

print(person)
#automobile[input("create automobile: " )] = input("new item : ")
text = input("enter new item :")
pair = text.split(",")
key, value = pair

person[key] = value 

print(person)
