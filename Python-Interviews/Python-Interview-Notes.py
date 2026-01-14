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

# What is global and local variable?
"""
1. Global variable is accessible everywhere
2. local variable is accessible only inside a function or block.
"""

# Example 
name = "Eshwar"
print(name)
print(type(name))

# What is type() function ?
"""Type function converts one data type to another data type"""

#--------------------------------------------------------------------------------------------------
# CHAPTER-3 : DATA TYPES IN PYTHON

# What is data type in python ?
"""Data type represents the different kinds of values that we stored on the variable"""

# Why called python is a dynamically typed  language ?
"""No need to specify the data type explicitly, 
based on the values type python allocated automatically at the run time"""
