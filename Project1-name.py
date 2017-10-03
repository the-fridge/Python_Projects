# Author : Syed Marwan Jamal.
# This program asks for user name,
# the length of the name is also returned.
# Please give your feedback on the program and way to improve it.


print('Hello')
user_name = input('What is your name?\n') # Asks for user name. 
print('It\'s nice to meet you', user_name)
print('Length of your name is:')
print(len(user_name)) # Returns name's length

# Another way
print('Hello')
user_name = input('What is your name?\n') # Asks for user name.
name_size = len(user_name) # Name's length
msg = 'It\'s nice to meet you {0}!\nThe length of your name is: {1}'.format(user_name, name_size) # Formatting message
print(msg)
