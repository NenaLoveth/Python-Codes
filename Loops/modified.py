bank_name = 'ZENITH BANK'


def intro():
    welcome_note = 'Hi, welcome to the Zenith bank application'
    print(welcome_note)
    system_1 = 'what action would you like to perform'
    print(system_1)
    instruction = 'Each action to perform is represented by their corresponding numbers;choose from 0-6.'
    print(instruction)


def create_account():
    users_name = input('Enter your full name (BLOCK LETTERS): ').title()
    users_contact_number = int(input('Enter your phone number: '))
    users_sex = input('Enter your sex: ')
    users_age = int(input('Enter your age:'))
    print('Instruction: select account type from 0-2')
    account_type = ('savings: 1' + ',' + 'current: 2' + ',' + 'fixed: 3')
    print(account_type)
def savings_acct():
    print(account_number)
    print('Account name:' + users_name + '\n' + 'Account number:' + str(account_number))
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


def transfer():
    print('please, Enter recipient details')
    recipent_2_acct_number = int(input('Recipient No:'))
    amount_figures_2 = int(input('Enter amount in figures: '))
    recipient_2_acct_name = input('Enter recipients name: ')
    print('Please confirm your information')
    print('Name: ', recipient_2_acct_name + ';' + 'Account number: ', recipent_2_acct_number)
    print('Transaction in progress...please wait')
    print('Transaction complete|')


def options():
    print(
        'create account: 1' + ', '+ 'deposit: 2' +', '+ 'withdraw: 3' +', '+ 'transfer: 4' +', '+ 'check balance: 5' +','+ 'statement of account: 6' +', '+ 'exit:0')


def ezit():
    print('would you like to exit?')
    response = {'YES': 1, 'NO': 2}
    print(response)
    exitors_response = int(input('Enter your response: '))
    if exitors_response == 1:
        print('You have exited the options')
    elif exitors_response == 2:
        print('would you like to perform an action?')
def user_resp

# ZENITH BANK
intro()
options()
users_name = ""
account_number = 23456784999

operators_response = int(input('Enter option: '))
if operators_response == 1:
    create_account()
    users_response = int(input('Enter option: '))
    if users_response == 1:
        savings_acct()
    elif users_response == 2:
        current_acct()
    elif users_response == 3:
        fixed_acct()
    else:
        print('your input is not valid')
elif operators_response == 2:
    deposit()
elif operators_response == 3:
    withdraw()
elif operators_response == 4:
    transfer()
elif operators_response == 5:
    check_bal()
elif operators_response == 6:
    stat_of_acct()
elif operators_response == 0:
    ezit()
    options()
