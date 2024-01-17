# pattern.py

# number of rows in the pattern
num_rows = 5

# loop to iterate through each row
for row in range(1, num_rows * 2):

    # ternary operator to determine the number of stars in the line
    stars = row if row <= num_rows else (num_rows * 2 - row)
    
    # output the stars in the pattern
    print('*' * stars)
