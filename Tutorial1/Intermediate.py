airtime_balance = 50
account_balance = "your account balance is low please recharge as soon as possible, thank you"
bank_balance = 200
print(airtime_balance,",", account_balance, bank_balance)
if airtime_balance <= 50:
    account_balance = "your account balance is low please recharge as soon as possible, thank you"
    airtime_balance += 100
    bank_balance -= 100
print(airtime_balance,",", account_balance, bank_balance)
airtime_balance = 20
print(airtime_balance,",", account_balance, bank_balance)

airtime_balance = 40
account_balance = "your account balance is low please recharge as soon as possible, thank you"
bank_balance = 200
mtn_system="thank you for choosing mtn, your call is in the progress"
if airtime_balance <50:
    account_balance = "your account balance is low please recharge as soon as possible, thank you"
    airtime_balance += 100
    bank_balance -= 100
    print(airtime_balance, ",", account_balance, bank_balance)

elif airtime_balance >50:
    mtn_system = "thank you for choosing mtn, your call is in the progress"
    print(mtn_system)

airtime_balance=200
if airtime_balance <50:
    account_balance = "your account balance is low please recharge as soon as possible, thank you"
    airtime_balance += 100
    bank_balance -= 100
    print(airtime_balance, ",", account_balance, bank_balance)

elif airtime_balance >50:
    mtn_system = "thank you for choosing mtn, your call is in the progress"
    print(mtn_system)


sex= input('Enter your gender: ')
if sex=='male':
    print("hello, you\'re good looking")
elif sex=='female':
    print("hi, you\'re pretty")
else:
    print('unrecognized sex, don\'t you want to disclose your sex?')
weight = 42
height = 151
BMI = weight / (height / 100) ** 2
print(BMI)
if BMI < 18.5:
    print('BMI is below normal, INDICATING - UNDERWEIGHT')
elif BMI < 25 >= 18.5:
    print('BMI is considered normal, INDICATING - NORMAL WEIGHT')
elif BMI < 32 >= 25.5:
    print('BMI is above normal, INDICATING - OVERWEIGHT')
elif BMI > 32.5:
    print('OBESITY')

weight = float(input('Body weight: '))
height = float(input('Height: '))
BMI = weight / (height / 100) ** 2
print(BMI)
if BMI < 18.5:
    print('BMI is below normal, INDICATING - UNDERWEIGHT')
elif BMI < 25 >= 18.5:
    print('BMI is considered normal, INDICATING - NORMAL WEIGHT')
elif BMI < 32 >= 25.5:
    print('BMI is above normal, INDICATING - OVERWEIGHT')
elif BMI > 32.5:
    print('OBESITY')