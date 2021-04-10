grades = ["A", "B", "C", "D", "E"]
scores = grades
print("grades: ", scores)
names = "\n".join(["january", "february", "march", "april"])
print(names)
names = ["january", "february", "march", "april"]
print("\n".join(names))
print("\n" "-".join(names))

names = "i am a good girl"
print(names.title().islower())
print(names.capitalize())
print(names.upper())
print("i")

family = ['john', 'james', 'rita', 'felix']
family.append("jonathan")
print(len(family))
john_location = (12, 58)
print(type(john_location))
print("latiude to the north: {}".format(john_location[0]))
print("longitude to the south: {}".format(john_location[1]))

country = (0.878 / 2, 78 + 3)
print(type(country))
print(country)
country = 34, 76, 89
print(type(country))
nations = ['nigeria', 'ghana', 'senegal', 'togo', 'nigeria', 'sierra leone']
nation_set = set(nations)
print(len(nation_set))
print('togo' in nations)
print('india' in nation_set)
nation_set.add('india')
print('india' in nations)
print('india' in nation_set)
nation_set.pop()
print(nation_set)
element = {'hydrogen': 1, 'lithium': 3, 'beryllium': 4, 'carbon': 6}
element['potassium'] = 19
print(element)
print(element.get('lithium'))
element = {'hydrogen': {'number':1, 'symbol':'H'} , 'lithium': 3, 'beryllium': 4, 'carbon': 6}
print(element)
