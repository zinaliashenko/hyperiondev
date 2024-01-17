# cafe.py

# a list called menu
menu = ["Coffee", "Tea", "Juice", "Water"]

# a dictionary called stock with stock values for each item
stock = {"Coffee": 100, "Tea": 57, "Juice": 34, "Water": 111}

# a dictionary called price with prices for each item
price = {"Coffee": 2.76, "Tea": 1.57, "Juice": 5.52, "Water": 3.21}

# the total_stock worth in the cafe
total_stock_value = 0

# a loop through the menu list
for item in menu:
    item_value = stock[item] * price[item]
    total_stock_value += item_value

# print the result of the calculation
print(f"Total stock worth in the cafe: £{total_stock_value}")
