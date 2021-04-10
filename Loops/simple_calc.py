# SIMPLE CALCULATOR
def calculate():
    num1 = input('Enter a number:')
    operator = input('Enter any operator:')
    num2 = input('Enter another number:')
    if operator == "+":
        print(float(num1) + float(num2))
    elif operator == "-":
        print(float(num1) - float(num2))
    elif operator == "/":
        print(float(num1) / float(num2))
    elif operator == "*":
        print(float(num1) * float(num2))
    elif operator == "^":
        print(float(num1) ** float(num2))
    else:
        print("Invalid input")


ezit = 1
while ezit == 1:
    calculate()
    ezit = int(input("Enter 1 to continue 0 to exit"))
