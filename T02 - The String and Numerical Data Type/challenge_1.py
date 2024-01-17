# challenge_1.py

# enter the lengths of all three sides of a triangle
# convert variables to float
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# calculate the semi-perimeter
s = (side1 + side2 + side3) / 2

# calculate the area of the triangle
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

# print out the area of the triangle
print("The area of the triangle is: ", area)
