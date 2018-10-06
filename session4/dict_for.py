person = {
    'name': 'quan',
    'age' : 22,
    'location':'hanoi',
}
for x in person.keys():
    print(x,person[x])

# for v in person.values():
#     print(v)


for k,v in person.items():
    print(k, v,sep=": ")