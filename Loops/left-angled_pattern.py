star = '*'
max_star = 8
count = 7

while len(star) <= max_star:
    space = " " * count
    print(space + star)
    count -= 1
    star += '*'

star = star[:-1]
count = 0
while len(star) > 0:
    space = " " * count
    if len(star) != max_star:
        print(space + star)
    count += 1
    star = star[:-1]


