def intelligence(name, age, clas):
    score = 0
    score_two = 0
    if Age > 10:
        score = +1
    elif Age < 10:
        score = + 2
    if Clas > 6:
        score_two = + 2
    elif Clas < 6:
        score_two = + 1
    total = int(score) + int(score_two)
    print(total)
    if total > 3:
        print(Name +" " + "is intelligent")
    else:
        print( Name +" " + "is likely not to be intelligent")

Name = input("Enter your name:")
Age = int(input("Enter your age: "))
Clas = int(input("Enter class: "))
intelligence(Name,Age,Clas)

def create_account():
    users_name = input('Enter your full name (BLOCK LETTERS): ').title()
    users_contact_number = int(input('Enter your phone number: '))
    users_sex = input('Enter your sex: ')
    users_age = int(input('Enter your age:'))
    account_type = {'savings': 0, 'current': 1, 'fixed': 2}
    print(account_type)
    print('select account from 0-2')
    users_response = int(input('Enter option: '))
def savings_acct():
    print(account_number)
    print(account_number, ',', '\n', users_name)
    print('Thank you for choosing Zenith bank')
def current_acct():
    print(account_number)
    print(account_number)
    print(account_number, ',', '\n', users_name)
    print('Thank you for choosing Zenith bank')
def fixed_acct():
    print(account_number)
    print(account_number)
    print(account_number, ',', '\n', users_name)
    print('Thank you for choosing Zenith bank')
def deposit():
    print('Enter your details and recipient account number')
    depositors_name = input('Enter your full name (BLOCK LETTERS): ').upper()
    depositors_number = int(input('Enter your phone number'))
    recipients_acct_number = int(input('Enter recipients account number'))
    recipients_acct_name = input('Enter your full name (BLOCK LETTERS): ').upper()
    amount = int(input('Enter amount in figures: '))
    print('transaction complete|')
def withdraw():
    print('Enter amount in figures')
    amount_figures = int(input('Enter amount in figures: '))
    print('transaction in progress')
    print('transaction complete|')
    print('would you like to perform another action?')
def check_bal():
    print('system loading')
    print(users_name, account_number)
    print('please wait...')
    print('Your balance: ...........')
    print('would you like to perform another action?')
def stat_of_acct():
    print('please wait while the system processes your account statement')
    print('July: .....\n August:....\n September:...')
    print('would you like to perform another action?')
def end_prog():
    print('would you like to exit?')
    response = {'YES': 1, 'NO': 2}
    print(response)
    exitors_response = int(input('Enter your response: '))
    if exitors_response == 1:
        print('You have exited the options')
    elif exitors_response == 2:
        print('would you like to perform an action?')
        print(options)
        operators_response = int(input('Enter option: '))
        print(operators_response)
def options():
    {'create account': 1,
     'deposit': 2,
     'withdraw': 3,
     'transfer': 4,
     'check balance': 5,
     'statement of account': 6,
     'exit': 0}

