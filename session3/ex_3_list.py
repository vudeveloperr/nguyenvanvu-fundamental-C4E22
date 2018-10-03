items = ['asd', 'ert', 'rtyu', 'dfgh' ]
print(items)

print(*items, sep="| ")

newitems = input("add your favorite : ")
items.append(newitems)
print(*items, sep=", ")

p = int(input("p to read ?"))
print(items[p-1])

i = int(input("enter space : "))
print(items[i]) 
