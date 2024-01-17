# challenge_2.py

# enter the name of a user's favourite restaurant
string_fav = input("Enter your favorite restaurant: ")

# enter the user's favourite number
# convert int_fav to an integer
int_fav = int(input("Enter your favorite number: "))

# print out the favorite restaurant and number using two separate print statements
print("Your favorite restaurant:", string_fav)
print("Your favorite number:", int_fav)

# if I try to cast string_fav to an integer,
# this will result in a ValueError if the string contains non-numeric characters
int_from_string_fav = int(string_fav)
