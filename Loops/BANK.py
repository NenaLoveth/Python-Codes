bank_name = 'ZENITH BANK'
welcome_note = 'Hi, welcome to the Zenith bank application'
print(welcome_note)
system_1 = 'what action would you like to perform'
print(system_1)
instruction = 'Each action to perform is represented by their corresponding numbers;choose from 0-6.'
print(instruction)
options = {'create account': 1, 'deposit': 2, 'withdraw': 3, 'transfer': 4, 'check balance': 5,
           'statement of account': 6, 'exit': 0}
print(options)
users_name = ""
account_number = 23456784999

operators_response = int(input('Enter option: '))
print(operators_response)

if operators_response == 1:
    print('confirm you would like to create an account')
    users_name = input('Enter your full name (BLOCK LETTERS): ').title()
    users_contact_number = int(input('Enter your phone number: '))
    users_sex = input('Enter your sex: ')
    users_age = int(input('Enter your age:'))
    account_type = {'savings': 0, 'current': 1, 'fixed': 2}
    print(account_type)
    print('select account from 0-2')
    users_response = int(input('Enter option: '))
    if users_response == 0:
        print('savings')
        print(account_number)
        print(account_number,',','\n', users_name)
        print('Thank you for choosing Zenith bank')
    elif users_response == 1:
        print('current')
        print(account_number)
        print(account_number)
        print(account_number, ',', '\n', users_name)
        print('Thank you for choosing Zenith bank')
    elif users_response == 2:
        print('fixed')
        print(account_number)
        print(account_number)
        print(account_number, ',','\n', users_name)
        print('Thank you for choosing Zenith bank')
    else:
        print('your input is not valid')
elif operators_response == 2:
    print('Enter your details and recipient account number')
    depositors_name = input('Enter your full name (BLOCK LETTERS): ').upper()
    depositors_number = int(input('Enter your phone number'))
    recipients_acct_number = int(input('Enter recipients account number'))
    recipients_acct_name = input('Enter your full name (BLOCK LETTERS): ').upper()
    amount = int(input('Enter amount in figures: '))
    print('transaction complete|')
elif operators_response == 3:
    print('Enter amount in figures')
    amount_figures = int(input('Enter amount in figures: '))
    print('transaction in progress')
    print('transaction complete|')
    print('would you like to perform another action?')
elif operators_response == 4:
    print('please, Enter recipient details')
    recipent_2_acct_number = int(input('Recipient No:'))
    amount_figures_2 = int(input('Enter amount in figures: '))
    recipient_2_acct_name = input('Enter recipients name: ')
    print('Please confirm your information')
    print('Name: ', recipient_2_acct_name + ';' + 'Account number: ', recipent_2_acct_number)
    print('Transaction in progress...please wait')
    print('Transaction complete|')
elif operators_response == 5:
    print('system loading')
    print(users_name, account_number)
    print('please wait...')
    print('Your balance: ...........')
    print('would you like to perform another action?')
elif operators_response == 6:
    print('please wait while the system processes your account statement')
    print('July: .....\n August:....\n September:...')
    print('would you like to perform another action?')
elif operators_response == 0:
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
        if operators_response == 1:
            print('confirm you would like to create an account')
            users_name = input('Enter your full name (BLOCK LETTERS): ').title()
            users_contact_number = int(input('Enter your phone number: '))
            users_sex = input('Enter your sex: ')
            users_age = int(input('Enter your age:'))
            account_type = {'savings': 0, 'current': 1, 'fixed': 2}
            print(account_type)
            users_response = int(input('Enter option: '))
            if users_response == 0:
                print('savings')
                print(account_number)
                print(account_number, ',', '\n', users_name)
                print('Thank you for choosing Zenith bank')
            elif users_response == 1:
                print('current')
                print(account_number)
                print(account_number)
                print(account_number, ',', '\n', users_name)
                print('Thank you for choosing Zenith bank')
            elif users_response == 2:
                print('fixed')
                print(account_number)
                print(account_number)
                print(account_number, ',', '\n', users_name)
                print('Thank you for choosing Zenith bank')
            else:
                print('your input is not valid')
        elif operators_response == 2:
            print('Enter your details and recipient account number')
            depositors_name = input('Enter your full name (BLOCK LETTERS): ').upper()
            depositors_number = int(input('Enter your phone number'))
            recipients_acct_number = int(input('Enter recipients account number'))
            recipients_acct_name = input('Enter your full name (BLOCK LETTERS): ').upper()
            amount = int(input('Enter amount in figures: '))
            print('transaction complete|')
        elif operators_response == 3:
            print('Enter amount in figures')
            amount_figures = int(input('Enter amount in figures: '))
            print('transaction in progress')
            print('transaction complete|')
            print('would you like to perform another action?')
        elif operators_response == 4:
            print('please, Enter recipient details')
            recipent_2_acct_number = int(input('Recipient No:'))
            amount_figures_2 = int(input('Enter amount in figures: '))
            recipient_2_acct_name = input('Enter recipients name: ')
            print('Please confirm your information')
            print('Name: ', recipient_2_acct_name + ';' + 'Account number: ', recipent_2_acct_number)
            print('Transaction in progress...please wait')
            print('Transaction complete|')
        elif operators_response == 5:
            print('system loading')
            print(users_name, account_number)
            print('please wait...')
            print('Your balance: ...........')
            print('would you like to perform another action?')
        elif operators_response == 6:
            print('please wait while the system processes your account statement')
            print('July: .....\n August:....\n September:...')
            print('would you like to perform another action?')
        elif operators_response == 0:
            print('would you like to exit?')
            response = {'YES': 1, 'NO': 2}
            if response == 1:
                print('You have exited the options')
            elif response == 2:
                print('would you like to perform an action?')
                print(options)
                operators_response = int(input('Enter option: '))
else:
    print('INVALID INPUT')
    print(options)
    operators_response = int(input('Enter option: '))
    print(operators_response)

    if operators_response == 1:
        print('confirm you would like to create an account')
        users_name = input('Enter your full name (BLOCK LETTERS): ').title()
        users_contact_number = int(input('Enter your phone number: '))
        users_sex = input('Enter your sex: ')
        users_age = int(input('Enter your age:'))
        account_type = {'savings': 0, 'current': 1, 'fixed': 2}
        print(account_type)
        users_response = input('Enter option: ')
        if users_response == 0:
            print('savings')
            print(account_number)
            print('Your account details are: ' + ' ' + 'acct number: ', account_number, +' ' + 'account name: ',
                  users_name)
            print('Thank you for choosing Zenith bank')
        elif users_response == 1:
            print('current')
            print(account_number)
            print('Your account details are: ' + ' ' + 'acct number: ', account_number, +' ' + 'account name: ',
                  users_name)
            print('Thank you for choosing Zenith bank')
        elif users_response == 2:
            print('fixed')
            print(account_number)
            print('Your account details are: ' + ' ' + 'acct number: ', account_number, +' ' + 'account name: ',
                  users_name)
            print('Thank you for choosing Zenith bank')
        else:
            print('your input is not valid')
    elif operators_response == 2:
        print('Enter your details and recipient account number')
        depositors_name = input('Enter your full name (BLOCK LETTERS): ').upper()
        depositors_number = int(input('Enter your phone number'))
        recipients_acct_number = int(input('Enter recipients account number'))
        recipients_acct_name = input('Enter your full name (BLOCK LETTERS): ').upper()
        amount = int(input('Enter amount in figures: '))
        print('transaction complete|')
    elif operators_response == 3:
        print('Enter amount in figures')
        amount_figures = int(input('Enter amount in figures: '))
        print('transaction in progress')
        print('transaction complete|')
        print('would you like to perform another action?')
    elif operators_response == 4:
        print('please, Enter recipient details')
        recipent_2_acct_number = int(input('Recipient No:'))
        amount_figures_2 = int(input('Enter amount in figures: '))
        recipient_2_acct_name = input('Enter recipients name: ')
        print('Please confirm your information')
        print('Name: ', recipient_2_acct_name + ';' + 'Account number: ', recipent_2_acct_number)
        print('Transaction in progress...please wait')
        print('Transaction complete|')
    elif operators_response == 5:
        print('system loading')
        print(users_name, account_number)
        print('please wait...')
        print('Your balance: ...........')
        print('would you like to perform another action?')
    elif operators_response == 6:
        print('please wait while the system processes your account statement')
        print('July: .....\n August:....\n September:...')
        print('would you like to perform another action?')
    elif operators_response == 0:
        print('would you like to exit?')
        response = {'YES': 1, 'NO': 2}
        if response == 1:
            print('You have exited the options')
        elif response == 2:
            print('would you like to perform an action?')
            print(options)
            operators_response = int(input('Enter option: '))
