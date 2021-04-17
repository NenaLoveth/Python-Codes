ticket = 1200
n_pass = 0
count = 0
passengers = []
while n_pass < 7:
    p_age = int(input('Enter your age: '))
    # p_name = input('Enter your name: ')
    passengers.append(p_age)
    n_pass += 1
print(passengers)
for age in passengers:
    if age < 1:
        print('Ticket is free')
    else:
        count += 1
print('passengers >= 1: ', count)
print(count * ticket)

