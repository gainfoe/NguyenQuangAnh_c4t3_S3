inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

print("Them key 'pocket':")
inventory['pocket'] = []
for i in inventory:
    print(i, ":", end=" ")
    try:
       print(*inventory[i], sep=", ")
    except:
        print(inventory[i])
print()

print("Them item vao key 'pocket':")
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
for i in inventory:
    print(i, ":", end=" ")
    try:
       print(*inventory[i], sep=", ")
    except:
        print(inventory[i])
print()

print("Xoa item 'dagger':")
inventory['backpack'].remove('dagger')
for i in inventory:
    print(i, ":", end=" ")
    try:
       print(*inventory[i], sep=", ")
    except:
        print(inventory[i])
print()

print("Them 50 vao 'gold':")
inventory['gold'] += 50
for i in inventory:
    print(i, ":", end=" ")
    try:
       print(*inventory[i], sep=", ")
    except:
        print(inventory[i])
