# WHILE LOOP
# Mixed Break and Continue
i = 1
while i < 10:
    if i == 9:
        break
    print(i)
    i += 1
r = 0
while r <= 27:
    if r == 7:
        r += 1
        continue
    print(r)
    r += 1
fruits = ['apple', 'orange', 'paw-paw', 'lemon']
foods = ['orange', 'onion', 'lemon', 'apple']
fruit_count = 0
for food in foods:
    if food not in fruits:
        print('Not a fruit')
        continue
    fruit_count += 1
    print('Found a fruit')
print('total fruit:', fruit_count)
# BREAK
manifest = [('buns', 30), ('corn', 65), ('beans', 70), ('potatoes', 103)]
weight = 0
items = []
for shippings in manifest:
    print('current weight: {}'.format(weight))
    if weight >= 110:
        print('the loop will break')
        break
    else:
        items.append(shippings[0])
        sums = weight + shippings[1]
        if sums >= 110:
            break
        else:
            weight = sums

print(weight)
print(items)
# ZIP AND UNZIP
manifest = [('buns', 30), ('corn', 65), ('beans', 70), ('potatoes', 103)]
item, weight = zip(*manifest)
print(item)
print(weight)
manifest=[]
for shippings in zip(item, weight):
    manifest.append(shippings)
    print(shippings[0], shippings[1])
print(manifest)
# ENUMERATE
fruits = [('beans', 13), ('plantain', 45), ('potatoes', 57), ('cassava', 70)]
quantity = []
for i, package in zip(range(len(fruits)), fruits):
    print(i, package)
# LIST COMPREHENSION
fruits = ['apple', 'orange', 'paw-paw', 'lemon']
Fruits = [fruit.title() for fruit in fruits]
print(Fruits)

squares = [r ** 3 for r in range(8)]
print(squares)
squares = [r ** 3 for r in range(8) if r % 2 == 0]
print(squares)
squares = [r ** 3 if r % 2 == 0 else r + 1 for r in range(8)]
print(squares)
