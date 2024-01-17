# while.py

# initialize variables
total = 0
count = 0

# asking the user to enter a number until -1 is entered
while True:
    user_input = input("Enter a number (or -1 to exit): ")

    if user_input == "-1":
        break

    # convert the user input to a float and update total and count
    number = float(user_input)
    total += number
    count += 1

# calculate the average
if count > 0:
    average = total / count
    print("The average of the entered numbers is:", average)
else:
    print("No valid numbers were entered.")
