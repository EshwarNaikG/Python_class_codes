# CHAPTER-1: PYTHON INTRODUCTION
# What is python ?
"""Python is a high-level, interpreted, object-oriented programming language known for its simple syntax 
and readability.
=> Developed by Guide van russam in 1991.
"""

# What are the features of Python?
"""
Simple syntax and Easy to learn

Interpreted language

Object-oriented Programming language

Dynamically typed language

Platform independent

Large standard library

"""
# Is Python compiled or interpreted?
"""Python is an interpreted language (internally compiled to bytecode).
Code executes line by line. """

# What is PEP 8?
"""PEP 8 is Python’s official coding style guide."""

# What is comments in python ?
"""
In python, comments are used to add notes OR explainations to the code.

Comments are ignored by the interpreter and are only visible in the code.
"""

# Types of comments - 2
"""
1. Single line comments.
2. Multi-line comments.
"""

# Single-Line comments.
"""Single-Line comments start with the # symbol and continue until the end of the line """

# Multi-Line Comments
"""Multi-line comments are enclosed in the triple quotes (""" """  OR  ''' ''')"""


#Why use comments
"""
1. Code readability :- Comments help others understand our code.

2. Debugging :- Comments can help us to identify issues or bugs in our code.

3. Documentation :- Comments can save as documentation for our code.
"""

# What is indentation in Python?
"""Indentation defines code blocks. Python uses indentation instead of braces {}"""

# What is type casting?
"""Type casting is converting one data type into another data type."""
# OR
"""Type casting is the manual conversion of one data type into another data type
 using Python’s built-in functions."""

n1 = int(input("Enter first number : "))   # converting string into integer# 
n2 = int(input("Enter second number : "))  # converting string into integer# 

# Note:-  User input values always return in string.

# What is None in Python?
"""None represents the absence of a value."""

# What is a keyword in Python? 
"""Keywords are the reserved words in python."""
import keyword
print(keyword.kwlist)

#------------------------------------------------------------------------------------------------

# CHAPTER-2 : VARIABLES IN PYTHON

# What is variable in python ?
"""Variable is a container used to stored  different types of values"""
# OR
"""Variable is the the name of memory location where we stored differnt types values"""

# Example 
name = "Eshwar"
print(name)
print(type(name))

# What is global and local variable?
"""
1. Global variable is accessible everywhere
2. local variable is accessible only inside a function or block.
"""
# Example:- GLOBAL VARIABLE..............................
x = 10   # global variable

def show():
    print(x)

show()
print(x)

# Exmaple:- LOCAL VARIABLE...................................
def display():
    y = 20   # local variable
    print(y)

display()
# print(y)  ❌ Error


# What is type() function ?
"""The type() function is used to find the data type of a variable or value."""

# Example 
name = "Eshwar"
print(name)
print(type(name))

#--------------------------------------------------------------------------------------------------

# CHAPTER-3 : DATA TYPES IN PYTHON

# What is data type in python ?
"""Data type represents the different kinds of values that we stored on the variable"""

# Why called python is a dynamically typed  language ?
"""No need to specify the data type explicitly, 
based on the values type python allocated automatically at the run time"""

x = 10      # int
z = 7.5     # float
y = "Hi"    # str

# Dtatypes 
"""
1. Int  
2. Float
3. Complex
4. String
5. Boolean
6. None    ====>>> None represents the absence of a value.
7. List
8. Tuple
9. Set
10. Dictionary (dict)
"""
# What are the built-in data types in Python?
"""
Python has the following built-in data types:

Numeric → int, float, complex

Sequence → list, tuple, range

Text → str

Set → set, frozenset

Mapping → dict

Boolean → bool
"""

# What is the difference between mutable and immutable data types?
"""
|   Mutable       |   Immutable            |
| --------------- | ---------------------- |
| Can be changed  | Cannot be changed      |
| list, set, dict | int, float, str, tuple |

"""
# Examples 
# Mutable
lst = [1, 2]
lst.append(3)

# Immutable
s = "Hi"
# s[0] = "h" ❌

# What is an int data type?
"""Used to store whole numbers."""
x = 100

# What is a float data type?
"""Stores decimal values."""
price = 99.99

# What is a string (str)?
"""A string is an immutable sequence of characters enclosed in single quotes, double quotes, 
or triple quotes."""
# Example
name = "Python"

# What is Type casting in Python ?
"""Type casting is the manual conversion of one data type into another data type
 using Python’s built-in functions."""

# Examples

a = 4   # int
b = "7.8"  # str
c = float(b)  # convert string into float
sum = a + c
print(sum)


# Note:-  User input values always return in string.

n1 = int(input("Enter first number : "))   # converting string into integer# 
n2 = int(input("Enter second number : "))  # converting string into integer# 

# What is the input() function in Python?
"""In Python the input() function is used to take input from the user during program execution."""

# Important Point
"""The input() function always returns a string, even if the user enters a number."""
