# finance_calculators.py

import math

# display menu to the user
print("Welcome to the Finance Calculators program!")

print("Menu:")
print("1. Investment - to calculate interest on investment")
print("2. Bond - to calculate bond repayment")

# input user's choice
user_choice = input("Enter 'investment' or 'bond' from the menu above to proceed: ").lower()

# process user's choice
if user_choice == "investment":
        
    # get user inputs for investment calculation
    amount = float(input("Enter the amount of money you are depositing: "))
    rate = float(input("Enter the interest rate (as a percentage): ")) / 100
    years = int(input("Enter the number of years you plan on investing: "))
    interest = input("Enter 'simple' or 'compound' interest: ").lower()

    # perform calculation based on interest type
    if interest == "simple":
        result = round(amount * (1 + rate * years), 2)
    elif interest == "compound":
        result = round((amount * math.pow((1 + rate), years)), 2)

    # display result
    print("The total amount after", years, "years will be:", result, 'pounds')

elif user_choice == "bond":
        
    # get user inputs for bond repayment calculation
    present_value = float(input("Enter the present value of the house: "))
    rate = float(input("Enter the annual interest rate: ")) / 100
    months = int(input("Enter the number of months for repayment: "))

    # perform bond repayment calculation
    monthly_interest_rate = rate / 100 / 12
    repayment = round((monthly_interest_rate * present_value) / (1 - math.pow((1 + monthly_interest_rate), -months)), 2)

    # display result
    print("The monthly bond repayment will be:", repayment, 'pounds')

else:
    print("Invalid choice. Please enter either 'investment' or 'bond'.")
