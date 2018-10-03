#khoi tao 1 list
#in ra list

items = ['qwert', 'asdfgh', 'zxcvb', 'poiuyt']
print(*items, sep= ", ")

items.append(input("add your favorite : "))
print(*items, sep=", ")

i = input("delete your space choose ")
if i.isdigit():
    p = int(i)
    items.pop(p-1)
    print(*items, sep=", ")
else:
    items.pop(input("delete you choose "))
    print(*items, sep=", ")    

