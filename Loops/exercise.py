import random

# Guessing numbers
print("WELCOME TO THE NUMBER GUESS!!!")
print("Choose randomly between 0-100 to guess the developer\'s choice number \n You have only 3 attempts.")
number =  random.randint(0,100)
attempt = 0
l_attempt = 0
while attempt < 7:
    guess = int(input("Please  input a number between 0 and 100: "))
    if guess == number:
        print("You got the right number!!!" + " " + str(number) + " " + "was the right number")
        print("Thank you for playing Number Guess.\n See you again.")
        break
    elif guess < number:
        print("This is less than actual number.")

    elif guess > number and guess < 100:
        print("This is greater than actual number.")
    else:
        print("The number is out of range")

    attempt += 1
    l_attempt= 7 - attempt
    print("Note: You have made " + str(attempt) + " " + "attempt")
    print("You have " + str(l_attempt) + " " + "left")

if attempt == 7:
    print("You have exceeded the attempt \n You couldn\'t guess the number"+" " + str(number))