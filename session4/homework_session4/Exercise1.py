inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
print(inventory)

# add pocket
inventory['pocket'] = [ 'seashell', 'strange berry', 'lint']
print(inventory)

#delete dagger in list backpack
del inventory['backpack'][1]
print(inventory)

#add 50 in gold
inventory['gold'] += 50
print(inventory)