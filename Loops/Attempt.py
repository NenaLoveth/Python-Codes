def fizz_buzz(num1):
    if num1 % 3 == 0 and num1 % 5 == 0:
        print("Number is divisible by 3 and 5")
        return "fizz buzz"
    elif num1 % 3 == 0:
        print("Number is divisible by 3 but not 5")
        return "fizz"
    elif num1 % 5 == 0:
        print("Number is divisible by 5 but not 3")
        return "buzz"
    else:
        print("Number is neither divisible by 3 nor 5")
        return num1


num = int(input("Enter any number: "))
print(fizz_buzz(num))

