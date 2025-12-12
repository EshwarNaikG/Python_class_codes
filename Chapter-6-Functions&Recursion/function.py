# What is Function in Python?
# A function is a block of reusable code that performs a specific task.
# It helps in organizing code, improving readability, and avoiding repetition.
# Functions can take inputs (parameters) and can return outputs (return values).

# # Syntax of Function
'''
def function_name(parameters):'''
    # code block to be executed
    # return value

# # Example of Function
def greet(name):
    """This function greets the person passed in as a parameter."""
    return f"Hello, {name}!"
# Calling the function
print(greet("Alice"))  # Output: Hello, Alice!

# # Example 2: Function with multiple parameters
def add(a,b):
    """This function returns the sum of two numbers."""
    sum = a + b
    return sum
# Calling the function
result = add(5, 3)
print("Sum is:", result)  # Output: Sum is: 8   

# # Example 3: Function without parameters
def say_hello(name):
    """This function says hello to the user."""
    return f"Hello,{name} !"
# Calling the function without argument
print(say_hello("Eshwar Naik G"))  # Output: Hello, Guest!

# PRACTICE
# 1. Write a function to calculate the factorial of a number
def factorial(n):
    """This function returns the factorial of a number n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Calling the function
print("Factorial of 5 is:", factorial(5))  # Output: Factorial of 5 is: 120

# OR
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)
# Calling the function
print("Factorial of 6 is",fact(6))  # Output: 720



