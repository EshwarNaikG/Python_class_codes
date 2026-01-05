# What is the input() function in Python?
"""In Python the input() function is used to take input from the user during program execution."""

# Important Point
"""The input() function always returns a string, even if the user enters a number."""


# Examples-1

# name = input("Enter your name : ")
# print(type(name), f" Hi Good morning {name}")
#-------------------------------------------------

#Example-2
# num = input("Enter your number : ")
# print(type(num), f"number is : {num}")
#------------------------------------------

# Type-Casting :

# n1 = int(input("Enter your first number : "))  # Convert str into int
# print(type(n1), n1)

# n2 = float(input("Enter your second number : ")) # Convert str into float
# print(type(n2), n2)

# print(f"sum of {n1} and {n2} is : {n1+n2}")

#---------------------------------------------------

# Find the area of Square 
side = int (input("Enter a side of a square : "))
area = side * side
A = side ** 2
print(f"The Area of square is : {area}")
print(A)
