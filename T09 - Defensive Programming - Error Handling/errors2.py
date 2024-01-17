# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = 'Lion' # Name Error: name 'Lion' needs to be in quotes
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" # Logical Error: needs using f-string to embed expressions inside string literals + Logical Error: the variables 'number_of_teeth' and 'animal_type' need to be swapped, because the logic is lost

print(full_spec) # Syntax Error: 'print' needs to be in parentheses

