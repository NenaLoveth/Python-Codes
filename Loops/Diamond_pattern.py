star = '*'
max_star = 12
count = 5
while len(star) < max_star:
    space = " " * count
    count -= 1
    print(space + star)
    star += '*' * 2
count = 0
star = star[:-2]
while len(star) > 0:
    space = " " * count
    if len(star) < (max_star -1):
        print(space + star)
    count += 1
    star = star[:-2]
