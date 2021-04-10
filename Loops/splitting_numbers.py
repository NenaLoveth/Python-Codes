import random
v = (int)(7.545)
c = str(7.5348)
d = c.split('.')
print(d)
print(d[1])
print(v)
list = random.randint

def user_msg(num):
    val =(int)(num)
    if val%2 == 0:
        print("number is an even number")
    else:
        print("nuumber is an odd number")
    return val

num1= (float(input("Enter any number:")))
print(user_msg(num1))
