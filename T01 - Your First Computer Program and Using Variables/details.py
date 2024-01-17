'''
Pseudo code for details.py

request input from the user
store input into variable called 'name'

request input from the user
store input into variable called 'age'

request input from the user
store input into variable called 'house_number'

request input from the user
store input into variable called 'street_name'

output the f-string with 'name', 'age', 'house_number', 'street_name'
'''

# prompt the user for their name
name = input("Enter your name: ")

# prompt the user for their age
age = input("Enter your age: ")

# prompt the user for their house number
house_number = input("Enter your house number: ")

# prompt the user for their street name
street_name = input("Enter your street name: ")

# print a sentence containing all the details
print(f"This is {name}. He is {age} years old and lives at house number {house_number} on {street_name}.")
