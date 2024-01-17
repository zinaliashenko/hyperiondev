# manipulation.py

str_manip = input("Enter a sentence: ")

# the length of str_manip
length_of_str = len(str_manip)
print("Length of str_manip:", length_of_str)

# replace every occurrence of the last letter with @
last_letter = str_manip[-1]
str_manip_replaced = str_manip.replace(last_letter, '@')
print("Modified str_manip:", str_manip_replaced)

# print the last 3 characters in str_manip backwards
last_three_backwards = str_manip[-3:][::-1]
print("Last 3 characters backwards:", last_three_backwards)

# Create a five-letter word using the first three and last two characters in str_manip
five_letter_word = str_manip[:3] + str_manip[-2:]
print("Five-letter word:", five_letter_word)
