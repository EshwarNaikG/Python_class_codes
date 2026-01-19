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

#---------------------------------------------------------------------------------------

# CHAPTER-4 :  INPUT() FUNCTION IN PYTHON

# What is the input() function in Python?
"""Input() function is used to take input from the user during program execution."""

# Important Point
"""The input() function always returns a string, even if the user enters a number."""

# Example
name = input("Enter your name : ")
age = input("Enter ypur age : ")

n1 = int(input("Enter first number : "))   # converting string into integer# 
n2 = int(input("Enter second number : "))  # converting string into integer# 


#---------------------------------------------------------------------------------------------

# CHAPTER-5 : OPERATORS IN PYTHON

# What is operator in python ?
"""An operator is a symbol that performs a certain operation between operands."""

# Types of Operators
"""
1. Arithmetic Operators (+, -, *, /, %, **, //)
2. Relational / Comparison Operators (==, !=, >, <, >=, <=)
3. Assignment Operators (=, +=, -=, *=, /=, %=, **=)
4. Logical Operators (and, or , not)
"""
# Arithmetic Operators

# examples
a = 7
b = 2
sum = a+b                 # Addition operator
print(f" Addition : {sum}")

print(f"Subtraction : {a-b}")    # Subtraction operator
print(f"Multiplication {a*b}")   #Multiplication operator
print(f"Division {a/b}")         # Division operator
print(f"Exponention : {a**b}")   # Exponention operator
print(f"Floor Division : {a//b}") # FloorDivision operator
print(f"Remainder : {a % b}")     # Remainder

#....................................
# Relational / Comparision operator
a = 50
b = 20

print(a == b)  # False
print(a != b)
print( a > b)  #True
print(a < b)  # False
print(a >= b) # True
print(a <= b) # False

#........................................
# Assignment Operator
num = 10
print(num)

num = num + 10
num +=10
print(num)

num -= 10
print(num)

num *= 10
print(num)

num /= 3
print(num)

num %= 10
print(num)

num **= 2
print(num)
#.....................................
# Logical Operators

# NOT Operator
a = 10
b = 5
print(not(a>b))  # False
print(not(a<b))  # True

# AND Operator
C = 20
D = 8
E = 10
F = 30

print(C > D and E > F)  # statement1 is True and statement2 False => Final ans is False
print(C > D and E < F)  # statement1 is True and statement2 True => Final ans is True

# OR Operator
print(C > D or E > F)   # statement1 is True and statement2 False => Final ans is True
print(C > D or E < F)   # statement1 is True and statement2 True => Final ans is True
print(C < D or E > F)   # statement1 is False and statement2 False => Final ans is False


#--------------------------------------------------------------------------------------------------------

# CHAPTER-5 : STRINGS IN PYTHON

# What is string in python ?
"""A string is an immutable sequence of characters enclosed in single quotes, double quotes, 
or triple quotes."""

# OR
"""A string is a sequence of characters enclosed in single quotes (' '), double quotes (" "), 
or triple quotes (''' ''' / """ """)."""

# Example 
name = "Eshwar"

# Key Interview Points to Remember
"""
1. Strings are immutable

2. They are indexed

3. Stored as Unicode

4. Written using ' ', " ", or """ """
"""

# Are strings mutable or immutable in Python?
"""Strings are immutable, because their values cannot be changed after creation."""
# Example
s = "hello"
# s[0] = 'H' ❌ Error


# How do you access characters in a string?
"""Using indexing."""

# Example
s = "Python"
print(s[0]) # P
print(s[-1]) # n

# What is string slicing?
"""Slicing is used to extract a part of a string."""

# Syntax
""" string[start:end:step] """
# Example
s = "Python"
print(s[1:4])

# What is the difference between == and is for strings?
"""
1. == compares values

2. is compares memory locations
"""
# Example
a = "hi"
b = "hi"
print(a == b) # True
print(a is b) # May be True or False

# How do you find the length of a string?
"""Using len() function."""

# Example
s = "Python"
print(len(s))

# What is string concatenation?
"""Joining two or more strings using +."""

# Example
a = "Hello"
b = "World"
print(a + " " + b)

# How do you repeat a string?
"""Using * operator."""

# Example
s = "Hi"
print(s * 3)

# What are common string methods in Python?
"""
     Method	        Description
    lower() 	    Converts to lowercase
    upper()	        Converts to uppercase
    strip()	        Removes spaces
    replace()	    Replaces substring
    split()	        Splits string
    find()	        Finds substring
"""

# Difference between find() and index()?
"""
1. find() → returns -1 if not found

2. index() → raises error if not found
"""
# Example
s = "python"
print(s.find('z')) # -1
# print(s.index('z')) ❌ Error

# What is split() method?
"""Splits a string into a list."""

# Example
s = "Python is easy"
print(s.split())


# What is join() method?
"""Joins elements of a list into a string."""

# Example
words = ['Python', 'is', 'easy']
print(" ".join(words))

# What is string formatting?
"""Used to insert values into strings."""

# Example
# a) f-string (Recommended)
name = "Eshwar"
age = 22
print(f"My name is {name} and age is {age}")

# How do you reverse a string?
s = "Python"
print(s[::-1])

# How do you check if a string is palindrome?
s = "madam"
print(s == s[::-1])

# How do you count occurrences of a character?
s = "banana"
print(s.count('a'))

# What is strip(), lstrip(), rstrip()?
"""Removes spaces from string."""
s = " hello "
print(s.strip())
print(s.lstrip())
print(s.rstrip())

# How to check string type (numeric, alpha)?
s = "123"
print(s.isdigit())
print(s.isalpha())

# What are escape characters?
"""Special characters starting with \.
Examples:

\n → New line

\t → Tab
"""

print("Hello\nWorld")

# Is empty string allowed in Python?
"""Yes"""

# Example
s = ""
print(len(s))

#----------------------------------------------------------------------------------------------------------

# CHAPTER-6 : CONDITION STATEMENT IN PYTHON

# What is conditional statement in Python ?
""" Conditional statement  executes different code blocks 
based on whether a given condition is True or False. """

# if-elif-else (syntax)

"""
if (condition):
    statement1

elif (condition):
    statement2

else:
    statement3
"""

# Why are conditional statements used?
"""
1. To control the flow of execution

2. To perform decision-making

3. To execute code only when a condition is satisfied
"""

# Types of Conditional Statements in Python
# 1. if Statement
"""Executes a block of code only if the condition is true."""

# Example 
age = 20
if age >= 18:
    print("Eligible to vote")

# 📌 Interview Point:
"""If the condition is false, the code inside if will not execute."""

# 2. if-else Statement
"""Executes one block if the condition is true, otherwise executes the else block."""

# Example
num = 5
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 📌 Interview Point:
"""Ensures exactly one block is executed."""

# if-elif-else Statement
"""Used to check multiple conditions."""

# Example
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

# 📌 Interview Point:
"""
1. Conditions are checked top to bottom

2. Only the first true condition is executed
"""

# Nested if
"""An if statement inside another if. """

# Example
num = 10

if num > 0:
    if num % 2 == 0:
        print("Positive Even Number")

# 📌 Interview Point:
"""Used when one condition depends on another."""

# Conditional Operators Used
"""
| Operator | Meaning               |
| -------- | --------------------- |
| `==`     | Equal to              |
| `!=`     | Not equal             |
| `>`      | Greater than          |
| `<`      | Less than             |
| `>=`     | Greater than or equal |
| `<=`     | Less than or equal    |

"""

# Logical Operators in Conditions
"""
| Operator | Description                            |
| -------- | -------------------------------------- |
| `and`    | True if both conditions are true       |
| `or`     | True if at least one condition is true |
| `not`    | Reverses the condition                 |

"""

# Example
age = 25
if age > 18 and age < 60:
    print("Working age")

# Q1. What is the difference between if and if-else?
"""
Answer:

1. if executes code only when the condition is true.

2. if-else provides an alternative block when the condition is false.
"""

# Q2. Can we write multiple else blocks?
"""❌ No, only one else is allowed per if.
But we can use multiple elif blocks.
"""

# Q3. What is the difference between elif and else?
"""
1. elif checks another condition

2. else executes when none of the conditions are true
"""

# Q4. What happens if multiple conditions are true in if-elif-else?
"""Only the first true condition is executed."""

# Q5. Is indentation important in conditional statements?
"""
✅ Yes. Python uses indentation to define code blocks.
Incorrect indentation causes an IndentationError.
"""

# Q6. Can conditional statements be used without comparison operators?
"""Yes. Any boolean expression or variable can be used."""
#Example
is_logged_in = True
if is_logged_in:
    print("Welcome User")

# Q7. What is a ternary conditional statement?
"""A one-line conditional statement."""
# Example
result = "Pass" if marks >= 40 else "Fail"

# 📌 Interview Tip:
"""Also called conditional expression"""

#🔹 Common Interview Programs...............................
# ✔ Check largest of three numbers
a, b, c = 10, 20, 15

if a > b and a > c:
    print("a is largest")
elif b > c:
    print("b is largest")
else:
    print("c is largest")

# ✔ Check leap year
year = 2024

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")

#-------------------------------------------------------------------------------------------------------

# CHAPTER-7 : LIST IN PYTHON

# What is list in python ?
"""List is a built-in data types in Python used to store multiple values in a single variable.
Lists are ordered, mutable, and allow duplicate values."""

