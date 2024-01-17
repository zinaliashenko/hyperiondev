# alternative.py

# input a string
input_str = input("Enter a string: ")

# make each alternate character into an upper case character and each other alternate character into a lower case character
alternated_chars = ''.join([char.upper() if index % 2 == 0 else char.lower() for index, char in enumerate(input_str)])
print("Alternate characters result: ", alternated_chars)

# make each alternate word into an upper case word and each other alternate word into a lower case word
words = input_str.split()
alternated_words = ' '.join([word.lower() if index % 2 == 0 else word.upper() for index, word in enumerate(words)])
print("Alternate words result: ", alternated_words)
