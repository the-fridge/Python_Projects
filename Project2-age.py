# Author : Syed Marwan Jamal.
# This program asks for user age,
# returns their age in x years.
# Please give your feedback on the program and way to improve it.


print('Hello')
user_age = int(input('What is your age? \n'))
print('Oh so your age is', user_age)
years = int(input('Enter a number to know your age after that many years \n'))
print('You will be',years+user_age, 'in', years ,'years')


# Another way of doing
user_age = int(input('Hello!\nWhat is your age? '))
# Formatting will make the message looks better
response = 'Oh so your age is {0}.'.format(user_age)
print(response)
years = int(input('Enter a number to know your age after that many years: '))
print('You will be', years + user_age, 'in', years, 'years.')
