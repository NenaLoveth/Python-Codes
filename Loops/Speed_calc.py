import math

def drivers_speed(speed):
    speed_limit = 70
    demerit = 0
    if speed < speed_limit:
        return "OK"
    else:
        demerit += ((speed - speed_limit) / 5)
        if demerit > 12:
            return "License suspended"
        return "Points: " + str(math.ceil((demerit)))


speed = int(input("Enter speed: "))
print(drivers_speed(speed))
