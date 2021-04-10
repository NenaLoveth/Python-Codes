email_status = 'subscribe'
african_countries = ['nigeria', 'togo', 'sierra leone', 'senegal', 'liberia']
other_countries = ['jamaica', 'italy', 'canada', 'england']
country = 'togo'
if (country in african_countries and country not in other_countries) and email_status == 'subscribe':
    print('click on the link below to register')
elif (country in african_countries and country not in other_countries) and email_status == 'unsubscribe':
    print('subscribe to get notifications')
elif (country not in african_countries and country in other_countries) and email_status == 'subscribe':
    print('please your country is not eligible')
elif (country not in african_countries and country not in other_countries) and email_status == 'unsubscribe':
    print('click the subscribe button')
else:
    print('your input is not recognized')


email_status = 'unsubscribe'
country = input('enter your country: ')
if (country in african_countries and country not in other_countries) and email_status == 'subscribe':
    print('click on the link below to register')
elif (country in african_countries and country not in other_countries) and email_status == 'unsubscribe':
    print('subscribe to get notifications')
elif (country not in african_countries and country in other_countries) and email_status == 'subscribe':
    print('please your country is not eligible')
elif (country not in african_countries and country not in other_countries) and email_status == 'unsubscribe':
    print('click the subscribe button')
else:
    print('your input is not recognized')
weather='snow'
if weather=='snow' or'':
    print('what should i do')
else:
    print('ignore')
weather='rain'
if weather=='snow' or'':
    print('what should i do')
else:
    print('ignore')
