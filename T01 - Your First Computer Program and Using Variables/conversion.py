'''
Pseudo code for conversion.py

declare variable 'num1'
declare variable 'num2'
declare variable 'num3'
declare variable 'string1'

convert 'num1' to an integer
convert 'num2' to an float
convert 'num3' to an string
convert 'string1' to an integer

output the 'num1', 'num2', 'num3', 'string1' on separate lines using f-string
'''

# declare variables
num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"

# convert variables
# convert num1 to an integer
int_num1 = int(num1)

# convert num2 to a float
float_num2 = float(num2)

# convert num3 to a string
str_num3 = str(num3)

# convert string1 to an integer
int_string1 = int(string1)

# print out the variables on separate lines
print("Converted int_num1:", int_num1)

print("Converted float_num2:", float_num2)

print("Converted str_num3:", str_num3)

print("Converted int_string1:", int_string1)
