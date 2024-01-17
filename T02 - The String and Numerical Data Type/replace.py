# replace.py

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Reprint the sentence with exclamation marks replaced by blank spaces
sentence_replaced = sentence.replace("!", " ")
print(sentence_replaced)

# Reprint the sentence in uppercase
sentence_upper = sentence_replaced.upper()
print(sentence_upper)

# Print the sentence in reverse
sentence_reverse = sentence_upper[::-1]
print(sentence_reverse)
