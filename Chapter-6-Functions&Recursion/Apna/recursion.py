# What is recursion in python?
#==> Recursion is a programming technique where a function calls itself in order to solve a problem.
#  It is commonly used for problems that can be broken down into smaller, similar subproblems. 
# A recursive function typically has two main components: 
# a base case that stops the recursion and a recursive case that continues the recursion by calling the function itself with modified arguments.

#--------------------------------------------------------------------------------------

# Example of a simple recursive function to calculate the factorial of a number
def show(n):
    if n == 0:  # Base case to stop recursion
        return
    else:
        print(n)
        show(n-1)  # Recursive call with a decremented value
show(5)
print("-----")
show(7)


# OR

def show(n):
    if n < 0:  # Base case to stop recursion
        return
    print(n)
    show(n-1)

show(5)  # This will lead to infinite recursion and eventually a RecursionError
#--------------------------------------------------------------------------------------

def show(n):
    if n == 10:  # Base case to stop recursion
        return
    else:
        print(n)
        show(n+1)  # Recursive call with an incremented value
show(5)
print("-----")
show(7)

#--------------------------------------------------------------------------------------

# Example of a recursive function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case
# Testing the factorial function
print("Factorial of 5 is:", factorial(5))  # Output: 120
print("Factorial of 7 is:", factorial(7))  # Output: 504

#--------------------------------------------------------------------------------------

# Let's Practice
# 1. Write a recursive function to calculate the sum of first n natural numbers
def sum_natural(n):
    if n == 1:  # Base case
        return 1
    else:
        return n + sum_natural(n - 1)
    
sum_result = sum_natural(5)
print(f"Sum of first 5 natural numbers is: {sum_result}")  # Output: 15

sum_result = sum_natural(10)
print(f"Sum of first 10 natural numbers is: {sum_result}")  # Output: 55

#--------------------------------------------------------------------------------------

# write a recursive funtion to print list of n elements
def print_list_recursive(lst, index=0):
    if index >= len(lst):  # Base case
        return
    else:
        print(lst[index], end=" ")
        print_list_recursive(lst, index + 1)  # Recursive call with incremented index   
print_list_recursive([1, 2, 3, 4, 5])
print()  # for newline


#--------------------------------------------------------------------------------------

# 2. Write a recursive function to find the GCD (Greatest Common Divisor) of two numbers
def gcd(a, b):
    if b == 0:  # Base case
        return a
    else:   
        return gcd(b, a % b)  # Recursive case
gcd_result = gcd(48, 18)
print(f"GCD of 48 and 18 is: {gcd_result}")  # Output: 6


#--------------------------------------------------------------------------------------
# 3. Write a recursive function to print all elements of a list. 
# Hint: Use list and index as parameters.

def print_list(list, index):
    if (index == len(list)):
        return
    print(list[index])
    print_list(list, index + 1)

friuts = ['apple', 'banana', 'chikoo', 'mango']
print_list(friuts, 0)

print_list(['a', 'b', 'c', 'd', 'e'], 0)

#--------------------------------------------------------------------------------------