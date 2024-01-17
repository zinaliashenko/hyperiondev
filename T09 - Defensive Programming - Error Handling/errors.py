# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") # Syntax Error: 'print' needs to be in parentheses
print("\n") # Syntax Error: 'print' needs to be in parentheses + Syntax Error: no need an indent for 'print' function

# Variables declaring the user's age, casting the str to an int, and printing the result
age_str = "24" # Name Error: name 'age_Str' is not defined because '==' operator is a comparison operator, not '=' assignment operator + Logical Error: need to set the variable name in lower case
age = int(age_str) # Value Error: the string '24 years old' need to be '24' because the string cannot be directly converted to an integer because it contains non-numeric characters 
print("I'm" + ' ' + str(age) + ' ' + "years old.") # Type Error: all operands need to be of string type when using the '+' operator to concatenate strings, 'age' is int, not string; Logical Error: message does not have appropriate spacing requiring: + " " +

# Variables declaring additional years and printing the total years of age
years_from_now = "3"
total_years = age + int(years_from_now) # Type Error: both operands need to be numbers to use the '+' operator as mathematical addition

print("The total number of years: " + f"{total_years}") # Syntax Error: 'print' needs to be in parentheses; message does not have appropriate space: '...: ' + Logical Error: need using f-string to embed expressions inside string literals + Name Error: name 'answer_years' is not defined, correct variable name need to be 'total_years' as it was when assigned

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 # Name Error: name 'total' is not defined; Logical Error: correct variable name need to be 'total_years' as it was when assigned
print("In 3 years and 6 months, I'll be " + str(f'{total_months + 6}') + " months old") # Syntax Error: 'print' needs to be in parentheses + Type Error: all operands need to be of string type when using the '+' operator to concatenate strings, 'total_months' needs to be converted in str + Logical Error: needs to fix the formula to add 6 months using f-string

#HINT, 330 months is the correct answer

