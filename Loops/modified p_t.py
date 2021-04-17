'''
an airline ticketting that calculates the total cost for all tickets purchased.
The capacity of passenger the airplane can carry is maximum of 7 both children
and adults inclusive.
Note: Tickets for children less than age 1 are FREE
'''
p_ticket = 120
n_pass = 0
count = 0
passengers = {}
pass_ages = []
pass_name = []
while n_pass < 7:
    p_name = input('Enter your name: ')
    p_age = float(input('Enter your age: '))
    pass_ages.append(p_age)
    pass_name.append(p_name)
    for name,age in zip(pass_name,pass_ages):
        passengers[name] = age
    n_pass += 1
print(passengers)
for key, value in passengers.items():
    if value < 1:
        print('Ticket is free for {}'.format(key))
    else:
        count +=1
print('payments collected from:', count, 'passengers')
print('total amount collected: ', count*p_ticket)






