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

#======================================================================================================

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

#====================================================================================================

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

#================================================================================================

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


#=======================================================================================================

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


#==================================================================================================

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

#=====================================================================================================

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

#======================================================================================================

# CHAPTER-7 : LIST IN PYTHON

# What is list in python ?
"""List is a built-in data types in Python used to store multiple values in a single variable.
Lists are ordered, mutable, and allow duplicate values."""

# OR
""" List is a collection of items that is ordered, mutable and allows dublicates elements. 
List can hold different data types such as integer, float, string boolean and None. """

#Example:-1
my_list = [1, 2, 3, 'Python',["Eshwar", "Adithya", "Rekha"]]
# fruits = ["apple", "banana", ] 
# print(my_list)

# Example:-2
# marks = [99, 97, 98.7, 96.45, 88.78]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(len(marks))
# print(sum(marks))
# print(sorted(marks))
# fruits = ["apple", "banana","cherry" ]  


# 🔹 What is a List in Python?
"""
A list is a collection of items that is:
1. Ordered,
2. Mutable (can be changed),
3. Allows duplicate values, &
4. Can store multiple data types.
"""

# 🔹 How to create a List?
"""Using square brackets [] with comma-separated values."""

# Example
my_list = [1, 2, 3, 'Python', ["Eshwar", "Adithya", "Rekha"]]
print(my_list)

# 🔹 Creating a List
a = []                  # Empty list
b = [1, 2, 3]
c = list((4, 5, 6))     # Using list() constructor
print(a)
print(b)
print(c)

# 🔹 Accessing List Elements (Indexing)
"""Using positive and negative indexing.
1. Positive Indexing: 0, 1, 2, ...
2. Negative Indexing: -1, -2, -3, ...
"""

# Example
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])   # apple
print(fruits[-1])  # date


# 🔹 Slicing a List
"""Extracting a portion of the list using slicing syntax: list[start:end:step]"""
# Example
nums = [1, 2, 3, 4, 5]

print(nums[1:4])   # [2, 3, 4]
print(nums[:3])    # [1, 2, 3]
print(nums[::2])   # [1, 3, 5]
print(nums[-3:])   # [3, 4, 5]


# 🔹 List is Mutable
"""Lists can be modified after creation."""
# Example-1
fruits = ["apple", "banana", "cherry"]

fruits[0] = "orange" # Modify element at index 0
print(fruits)  # ['orange', 'banana', 'cherry']

fruits.append("grapes")  # Add element at the end
print(fruits)  # ['orange', 'banana', 'cherry', 'grapes']

fruits.insert(1, "pineapple") # Insert at index 1
print(fruits)  # ['orange', 'pineapple', 'banana', 'cherry', 'grapes']


# Example-2
nums = [10, 20, 30]

nums[1] = 200  # Modify element at index 1
print(nums)   # [10, 200, 30]

nums.append(40)  # Add element at the end
print(nums)   # [10, 200, 30, 40]

nums.insert(2, 25)  # Insert 25 at index 2
print(nums)   # [10, 200, 25, 30, 40]


# 🔹 List Methods
Cars = ["Maruthi", "Honda Suzuki", "Swift Dzire",]

# append :- Adds one element at the end of the list
Cars.append("BMW")
print(Cars)


# 📌 List Methods (Very Important 🔥)..............................

# ➕ Adding Elements
a = [1, 2]

a.append(3)        # Add at end
a.insert(1, 10)    # Add at index
a.extend([4, 5])   # Add multiple values
#.................................
a = [1, 2]
print(a)
a.append(3)        # Add at end
print(a)

a.insert(1, 10)    # Add at index
print(a)

a.extend([4, 5])   # Add multiple values
print(a)


# ❌ Removing Elements
a = [10, 20, 30, 20]

a.remove(20)   # Removes first occurrence
a.pop()        # Removes last element
a.pop(1)       # Removes index element
a.clear()      # Removes all elements
#.................................
a = [10, 20, 30, 20]
print(a)

a.remove(20)   # Removes first occurrence
print(a)

a.pop()        # Removes last element
print(a)

a.pop(1)       # Removes index element
print(a)

a.clear()      # Removes all elements
print(a)


# 🔍 Searching Elements
a = [1, 2, 3, 2, 4]
index = a.index(2)    # Get index of first occurrence
print(index)
count = a.count(2)    # Count occurrences
print(count)
#.................................
a = [10, 20, 30]

print(a.index(20))   # 1
print(a.count(20))   # 1
# ❗ Note: index() raises ValueError if not found


# 🔃 Sorting & Reversing
a = [3, 1, 4, 2]

a.sort()              # Ascending
a.sort(reverse=True) # Descending
a.reverse()
#.................................
a = [1, 5, 2, 0, 10, 3, 11 ,4]
a.sort()    # Sort in ascending order
print(a)

a.sort(reverse=True)  # Sort in Descending order
print(a)

a.reverse()
print(a)

# 📏 Length of List
a = [1, 2, 3, 4, 5]
length = len(a)
print(length)
#.................................
a = [10, 20, 30, 40, 50]
print(len(a))  # 5

# 📌 Looping Through List
# Using for loop
# Example-1
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example-2
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# Using indexing
# Example-1
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(fruits[i])

# Using while loop
# Example-2
numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

# 📌 List Comprehension (Advanced 🔥)

# Basic Syntax: [expression for item in iterable if condition]

# Example-1
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)  # [1, 4, 9, 16, 25]

# Example-2
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # [2, 4]

# Example-3
fruits = ["apple", "banana", "cherry"]
upper_fruits = [fruit.upper() for fruit in fruits]
print(upper_fruits)  # ['APPLE', 'BANANA', 'CHERRY']

# Example-4
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6]

# 📌 Nested List
# Example-1 
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])      # [1, 2, 3]
print(matrix[1][2])   # 6

# Example-2
teams = [
    ["Player1", "Player2", "Player3"],
    ["PlayerA", "PlayerB", "PlayerC"]
]
print(teams[0])      # ['Player1', 'Player2', 'Player3']
print(teams[1][1])   # PlayerB

# 📌 Copying a List
a = [1, 2, 3]
b = a.copy()      # Shallow copy
c = list(a)

# 📌 List vs Tuple (Interview Question)
"""
| List        | Tuple       |
| ----------- | ----------- |
| Mutable     | Immutable   |
| Uses [ ]    | Uses ( )    |
| Slower      | Faster      |
| More memory | Less memory |

"""

#📌 List Common Interview Questions.............................................................
# Q1: Is list mutable?
"""Yes, lists are mutable."""

# Q2: How to add an element to a list?
"""Using append(), insert(), or extend() methods."""

# Q3: How to remove an element from a list?
"""Using remove(), pop(), or clear() methods."""

# Q4: How to find the length of a list?
"""Using len() function."""

# Q5: How to sort a list?
"""Using sort() method or sorted() function."""

# Q6: How to reverse a list?
"""Using reverse() method or slicing."""

# Q7: How to check if an element exists in a list?
"""Using the in keyword."""

# Q8: How to copy a list?
"""Using copy() method or list() constructor."""

# Q9: What is list comprehension?
"""A concise way to create lists using a single line of code."""

# Q10: Can list store different data types?
"""Yes, lists can store different data types."""

# Q11: Difference between append() and extend()?
"""
1. append() → adds one element
2. extend() → adds multiple elements
"""

# Q12: Difference between remove() and pop()?
"""
1. remove() → removes by value
2. pop() → removes by index
"""

# Q13: How to create an empty list?
"""Using [] or list()."""

# Q14: How to access elements in a list?
"""Using indexing and slicing."""

# Q15: Can lists be nested?
"""Yes, lists can contain other lists as elements."""

# Q16: How to iterate through a list?
"""Using for loop or while loop."""

# Q17: What happens if you try to access an index that is out of range?
"""Raises an IndexError."""

# Q18: How to convert a tuple to a list?
"""Using list() constructor."""
my_tuple = (1, 2, 3)
my_list = list(my_tuple)

# Q19: How to convert a list to a tuple?
"""Using tuple() constructor."""
my_list = [1, 2, 3]
my_tuple = tuple(my_list)

# Q20: How to find the index of an element in a list?
"""Using index() method."""
my_list = [10, 20, 30]
index = my_list.index(20)  # 1  

# 🐍 Python List – Interview Questions & Answers.....................................................

# 🔹 1. What is a list in Python?
"""A list is a built-in data type in Python used to store multiple values in a single variable.
Lists are ordered, mutable, and allow duplicate values."""

a = [10, 20, "Python", 3.5]

# 🔹 2. Is a list mutable or immutable?
"""Lists are mutable, meaning their elements can be changed after creation."""
my_list = [1, 2, 3]
my_list[0] = 10  # Modifying the first element
print(my_list)  # Output: [10, 2, 3]

# 🔹 3. How do you create a list in Python?
"""Using square brackets [] with comma-separated values."""
fruits = ["apple", "banana", "cherry"]

# 🔹 4. Can a list store different data types?
"""Yes, lists can store different data types."""
mixed_list = [1, "hello", 3.5, True]

#🔹 5. What is indexing in a list?
"""Accessing elements using index values (starting from 0)."""
colors = ["red", "green", "blue"]
print(colors[1])  # Output: green

#🔹 6. What is negative indexing?
"""Accessing elements from the end of the list using negative index values (-1 for last element)."""
a = [10, 20, 30]
print(a[-1])   # 30
print(a[-2])   # 20
print(a[-3])   # 10

#🔹 7. What is slicing in a list?
"""Extracting a portion of the list using slicing syntax: list[start:end:step]"""
numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])   # [2, 3, 4]
print(numbers[:3])    # [1, 2, 3]
print(numbers[::2])   # [1, 3, 5]
print(numbers[-3:])   # [3, 4, 5]

#🔹 8. Difference between append() and extend()?
"""
1. append() → adds one element to the end of the list.
2. extend() → adds multiple elements from an iterable to the end of the list."""
# OR
"""
| append()            | extend()                |
| ------------------- | ----------------------- |
| Adds one element    | Adds multiple elements  |
| Adds as single item | Adds items individually |
"""
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

my_list.extend([5, 6])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

#🔹 9. Difference between remove() and pop()?
"""
1. remove() → removes the first occurrence of a specific value.
2. pop() → removes and returns the element at a specific index (default is last).
"""
# OR
"""
| remove()               | pop()                     |
| ---------------------- | ------------------------- |
| Removes by value       | Removes by index          |
| Removes first occurrence | Returns element at index  |
"""
my_list = [10, 20, 30, 20]
my_list.remove(20)
print(my_list)  # Output: [10, 30, 20]

my_list = [10, 20, 30, 20]
my_list.pop(1)
print(my_list)  # Output: [10, 30, 20]

# 🔹 10. What does clear() do?
"""clear() removes all elements from the list, resulting in an empty list."""
# OR
"""Removes all elements from the list."""
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []

#🔹 11. How to find the length of a list?
"""Using len() function."""
my_list = [1, 2, 3, 4, 5]   
print(len(my_list))  # Output: 5

# 🔹 12. How do you sort a list?
"""Using sort() method for in-place sorting or sorted() function to return a new sorted list."""
my_list = [3, 1, 4, 2]
my_list.sort()    # In-place sorting
print(my_list)    # Output: [1, 2, 3, 4]

my_list = [3, 1, 4, 2]
sorted_list = sorted(my_list)  # Returns a new sorted list  
print(sorted_list)  # Output: [1, 2, 3, 4]

# 🔹 13. How do you reverse a list?
"""Using reverse() method for in-place reversal or reversed() function to return a new reversed list."""
my_list = [1, 2, 3, 4]
my_list.reverse()    # In-place reversal
print(my_list)       # Output: [4, 3, 2, 1]

my_list = [1, 2, 3, 4]
reversed_list = list(reversed(my_list))   # Returns a new reversed list
print(reversed_list)   # Output: [4, 3, 2, 1]

# 🔹 14. How to check if an element exists in a list?
"""Using the 'in' keyword."""
my_list = [1, 2, 3, 4]
print(2 in my_list)   # Output: True
print(5 in my_list)   # Output: False

# 🔹 15. How to copy a list?
"""Using slicing [:] or copy() method."""
original_list = [1, 2, 3]
copied_list = original_list[:]  # Using slicing
print(copied_list)  # Output: [1, 2, 3]

original_list = [1, 2, 3]
copied_list = original_list.copy()  # Using copy() method
print(copied_list)  # Output: [1, 2, 3]

# 🔹 16. What is list comprehension?
"""List comprehension is a concise way to create lists. 
It allows you to generate a new list by applying an expression to each item in an existing iterable."""
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 🔹 17. Can lists be nested?
"""Yes, lists can contain other lists as elements."""
nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list)  # Output: [[1, 2], [3, 4], [5, 6]]

# 🔹 18. How to iterate through a list?
"""Using a for loop."""
my_list = [1, 2, 3, 4]
for item in my_list:
    print(item)

# 🔹 19. What happens if you try to access an index that is out of range?
"""If you try to access an index that is out of range, Python raises an IndexError."""
my_list = [1, 2, 3]
# print(my_list[5])  # IndexError: list index out of range



#===================================================================================================

# CHAPTER-8 : TUPLE IN PYTHON

# 1. What is tuple in python ?
"""Tuple is a built-in data types in Python used to store multiple values in a single variable
Tuples are ordered, immutable, and allow duplicate values."""

# OR
""" Tuple is a collection of items that is ordered, immutable and allows dublicates elements.
tuple can store multiple data typpes."""

# Example
my_tuple = (1, 2, 3, 'Python',("Eshwar", "Adithya", "Rekha"))
print(my_tuple)

# 2. How is a tuple different from a list?
"""
| Feature     | Tuple      | List         |
| ----------- | ---------- | ------------ |
| Mutability  | Immutable  | Mutable      |
| Syntax      | `()`       | `[]`         |
| Performance | Faster     | Slower       |
| Use case    | Fixed data | Dynamic data |
"""

# 3. How do you create a tuple?
"""Using parentheses () with comma-separated values."""
# Example
t1 = (10, 20, 30)
t2 = 10, 20, 30   # without parentheses
t3 = tuple((40, 50, 60))  # Using tuple() constructor
print(t1)
print(t2)
print(t3)

# 4. Can a tuple store different data types?
"""Yes, tuples can store different data types."""
mixed_tuple = (1, "hello", 3.5, True)

# 5. What is indexing in a tuple?
"""Accessing elements using index values (starting from 0)."""
colors = ("red", "green", "blue")
print(colors[1])  # Output: green

# 6. What is negative indexing?
"""Accessing elements from the end of the tuple using negative index values (-1 for last element)."""
a = (10, 20, 30)
print(a[-1])   # 30
print(a[-2])   # 20

# 7. What is slicing in a tuple?
"""Extracting a portion of the tuple using slicing syntax: tuple[start:end:step]"""
numbers = (1, 2, 3, 4, 5)
print(numbers[1:4])   # (2, 3, 4)
print(numbers[:3])    # (1, 2, 3)
print(numbers[::2])   # (1, 3, 5)
print(numbers[-3:])   # (3, 4, 5)

# 8. Is a tuple mutable or immutable?
"""Tuples are immutable, meaning their elements cannot be changed after creation."""
# Example
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This would raise a TypeError because tuples are immutable

# 9. How do you find the length of a tuple?
"""Using len() function."""
my_tuple = (1, 2, 3, 4, 5)   
print(len(my_tuple))  # Output: 5

# 10. How to check if an element exists in a tuple?
"""Using the 'in' keyword."""
my_tuple = (1, 2, 3, 4, 5)
print(3 in my_tuple)   # Output: True
print(6 in my_tuple)   # Output: False

# 11. How to convert a list to a tuple?
"""Using tuple() constructor."""
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)

# 12. How to convert a tuple to a list?
"""Using list() constructor."""
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  # Output: [1, 2, 3]

# 13. Can tuples be nested?
"""Yes, tuples can contain other tuples as elements."""
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple)  # Output: ((1, 2), (3, 4), (5, 6))

# 14. How to iterate through a tuple?
"""Using a for loop."""
my_tuple = (1, 2, 3, 4)
for item in my_tuple:
    print(item)

# 15. What happens if you try to access an index that is out of range?
"""If you try to access an index that is out of range, Python raises an IndexError."""
my_tuple = (1, 2, 3)
# print(my_tuple[5])  # IndexError: tuple index out of range

# 16. What is tuple unpacking?
"""Assigning elements of a tuple to multiple variables in a single statement."""
my_tuple = (10, 20, 30)
a, b, c = my_tuple
print(a)  # Output: 10
print(b)  # Output: 20
print(c)  # Output: 30

# 17. How to create a single-element tuple?
"""By adding a comma after the single element."""
single_element_tuple = (10,)
print(single_element_tuple)  # Output: (10,)

# 18. What are some common tuple methods?
"""Tuples have only two built-in methods: count() and index().

count() - Returns the number of occurrences of a value.
index() - Returns the index of the first occurrence of a value.
"""
my_tuple = (1, 2, 3, 2, 4)
print(my_tuple.count(2))  # Output: 2
print(my_tuple.index(3))  # Output: 2

# 19. How is a tuple different from a list?
"""
| Feature     | Tuple      | List         |

| ----------- | ---------- | ------------ |
| Mutability  | Immutable  | Mutable      |
| Syntax      | `()`       | `[]`         |
| Performance | Faster     | Slower       |
| Use case    | Fixed data | Dynamic data |
"""

# 20. When to use a tuple over a list?
"""Use a tuple when you need an immutable collection of items,
or when you want to ensure the data cannot be modified."""
# Example
coordinates = (10.0, 20.0)  # Using tuple for fixed coordinates
print(coordinates)

# 🟡 Intermediate Tuple Interview Questions

# 21. How do you access tuple elements?
"""Using indexing and slicing."""
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[2])    # Output: 30
print(my_tuple[1:4])  # Output: (20, 30, 40)

# 22. Can you change a tuple after it is created?
"""No, tuples are immutable and cannot be changed after creation."""
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This would raise a TypeError

# 23. How to concatenate two tuples?
"""Using the + operator."""
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# 24. How to repeat a tuple?
"""Using the * operator."""
my_tuple = (1, 2, 3)
repeated_tuple = my_tuple * 3
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)    

# 25. How to find the maximum and minimum values in a tuple?
"""Using max() and min() functions."""
my_tuple = (10, 20, 5, 30)
print(max(my_tuple))  # Output: 30
print(min(my_tuple))  # Output: 5

# 26. What happens if you try to modify a tuple?
"""If you try to modify a tuple, Python raises a TypeError because tuples are immutable."""
#OR
"""It raises a TypeError."""

t = (1, 2, 3)
t[0] = 5   # Error

my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This would raise a TypeError: 'tuple' object does not support item assignment

# 27. How do you loop through a tuple?
"""Using a for loop."""
# Example
my_tuple = (1, 2, 3, 4)
for item in my_tuple:
    print(item)

#Example
t = (1, 2, 3)
for i in t:
    print(i)


# 28. Can tuples contain mutable elements?
"""Yes, tuples can contain mutable elements like lists."""
my_tuple = (1, 2, [3, 4])
my_tuple[2][0] = 30  # Modifying the list inside the tuple
print(my_tuple)  # Output: (1, 2, [30, 4])

# 29. How to convert a string to a tuple?
"""Using tuple() constructor."""
my_string = "hello"
my_tuple = tuple(my_string)
print(my_tuple)  # Output: ('h', 'e', 'l', 'l', 'o')

# 30. How to convert a tuple to a string?
"""Using ''.join() method."""
my_tuple = ('h', 'e', 'l', 'l', 'o')
my_string = ''.join(my_tuple)
print(my_string)  # Output: hello   


# 🔵 Advanced Tuple Interview Questions..................................

# 31. How to unpack a tuple into variables?
"""By assigning the tuple to multiple variables."""
my_tuple = (10, 20, 30)
a, b, c = my_tuple
print(a)  # Output: 10
print(b)  # Output: 20
print(c)  # Output: 30

# 32. What are tuple packing and unpacking?
"""Tuple packing is the process of assigning multiple values to a single tuple variable.
Tuple unpacking is the process of assigning the elements of a tuple to multiple variables.
"""
# Packing
t = 1, 2, 3

# Unpacking
a, b, c = t
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# 33. How to slice a tuple?
"""Using the slicing syntax: tuple[start:end:step]"""
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[1:4])  # Output: (20, 30, 40)
print(my_tuple[:3])   # Output: (10, 20, 30)
print(my_tuple[::2])  # Output: (10, 30, 50)

# 34. Can you add elements to a tuple?
"""No, tuples are immutable and do not support adding elements directly."""
# However, you can create a new tuple by concatenation.
my_tuple = (1, 2, 3)
new_tuple = my_tuple + (4, 5)
print(new_tuple)  # Output: (1, 2, 3, 4, 5)

# 35. How to delete a tuple?
"""We cannot delete individual elements from a tuple,
 but we can delete the entire tuple using del statement."""
my_tuple = (1, 2, 3)
del my_tuple
# print(my_tuple)  # This would raise a NameError because the tuple is deleted

# 36. How to find the index of an element in a tuple?
"""Using index() method."""
my_tuple = (10, 20, 30, 20)
index = my_tuple.index(20)
print(index)  # Output: 1

# 37. How to count occurrences of an element in a tuple?
"""Using count() method."""
my_tuple = (1, 2, 2, 3, 2)
count = my_tuple.count(2)
print(count)  # Output: 3

# 38. How to create an empty tuple?
"""Using empty parentheses ()."""
empty_tuple = ()
print(empty_tuple)  # Output: ()

# 39. What built-in methods are available for tuples?
"""
Tuples support only two methods:
1. count() 
2. index()
"""
t = (1, 2, 2, 3)
print(t.count(2))   # 2
print(t.index(3))   # 3

# 40. Why are tuples faster than lists?
"""Tuples are faster than lists because they are immutable and have a smaller memory footprint."""

#OR
"""
Tuples are faster because:

1. They are immutable

2. Require less memory

3. No dynamic resizing
"""

# 41. Can a tuple be used as a dictionary key?
""""Yes, if it contains only immutable elements."""

d = {(1, 2): "value"}
print(d[(1, 2)])  # Output: value

# 42. How to convert a tuple to a dictionary?
"""Using dict() constructor with a list of key-value pairs."""
my_tuple = (("a", 1), ("b", 2), ("c", 3))
my_dict = dict(my_tuple)
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# 43. How do you delete a tuple?
"""You can delete the entire tuple using the del statement."""
# OR
"""We cannot delete individual elements, but we can delete the whole tuple using del statement."""
my_tuple = (1, 2, 3)
del my_tuple
# print(my_tuple)  # This would raise a NameError because the tuple is deleted

# 44. What is the difference between a tuple and a string?
"""
| Feature     | Tuple            | String          |
| ----------- | ---------------- | --------------- |
| Mutability  | Immutable        | Immutable       |
| Data Type   | Collection       | Sequence of chars|
| Use case    | Multiple values  | Text data       |
"""

# 45. What is the use of parentheses in a tuple?
"""Parentheses are used to define a tuple and group elements together."""
my_tuple = (1, 2, 3)
print(my_tuple)  # Output: (1, 2, 3)

# 46. What is the use of tuples in real applications?
"""Tuples are used for:
1. Storing fixed collections of items
2. Returning multiple values from functions
3. Using as dictionary keys
4. Data integrity (immutable data)
"""
# OR
"""
1. Returning multiple values from functions
2. Database records
3. Fixed configuration data
4. Dictionary keys
"""

# 47. Tuple vs List — when should you use tuple?
"""
Use a tuple when:

1. Data should not change

2. Performance is important

3. Data integrity is required
"""

# 48. Can tuples be nested within other tuples?
"""Yes, tuples can contain other tuples as elements."""
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple)  # Output: ((1, 2), (3, 4), (5, 6)) 

#===================================================================================================

# CHAPTER-9 : SET IN PYTHON

# What is set in python ?
"""A set is a collection of unique elements that is unordered, mutable (can be changed)
and do not allow duplicate values.
"""
#OR
"""A set is an unordered, mutable collection of unique elements."""


# ✅ Key Features of a Set
"""
✔ Stores only unique values (no duplicates)
✔ Unordered (no indexing or slicing)
✔ Mutable (you can add or remove elements)
✔ Written using curly braces {} or set() function
"""

# Example
my_set = {1, 2, 3, 'Python', {"Eshwar", "Adithya", "Rekha"}}
print(my_set)

# Example-2
fruits = {"apple", "banana", "cherry", "apple"}  # Duplicate "apple" will be ignored
print(fruits)  # Output: {'banana', 'cherry', 'apple'}

# Example-3
numbers = {1, 2, 3, 4, 5}
print(numbers)
print(type(numbers)) # <class 'set'>
print(len(numbers))  # 5

# 🔹 2. How to Create a Set?
"""Using curly braces {} with comma-separated values or using set() constructor."""
# Example-1
# Method 1: Using curly braces
my_set = {1, 2, 3, 'Python', {"Eshwar", "Adithya", "Rekha"}}
print(my_set)

# Example-2
fruits = {"apple", "banana", "cherry"}
print(fruits)

# Example-3
# Method 2: Using set() function
numbers = set([1, 2, 3, 4, 5])
print(numbers)

# 🔹 3. Can a set store different data types?
"""Yes, sets can store different data types."""
mixed_set = {1, "hello", 3.5, True}
print(mixed_set)  # Output: {1, 'hello', 3.5, True}

# 🔹 4. Are sets ordered or unordered?
"""Sets are unordered, meaning there is no index or order of elements in a set."""
# Example
my_set = {1, 2, 3}
# print(my_set[0])  # This would raise an error because sets are unordered

# 🔹 5. How to add elements to a set?
"""Use the add() method to add a single element to a set."""
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

# 🔹 6. How to remove elements from a set?
"""Use the remove() or discard() method."""
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}

# 🔹 7. What is the difference between remove() and discard()?
"""
- remove(): Raises KeyError if element is not found
- discard(): Does not raise an error if element is not found
"""
my_set.discard(5)  # No error even if element is not in the set
print(my_set)  # Output: {1, 3, 4}

# 🔹 8. How to find the length of a set?
"""Use the len() function."""
print(len(my_set))  # Output: 3

# 🔹 9. How to check if an element exists in a set?
"""Use the 'in' keyword to check if an element exists in a set."""
s = {1, 2, 3, 4, 5}
if 3 in s   :
    print("3 is in the set")
else:
    print("3 is not in the set")

# 🔹 10. How to clear a set?
"""Use the clear() method to remove all elements from a set."""
s = {1, 2, 3, 4, 5}
s.clear()
print(s)  # Output: set()   

# 🔹 11. Can sets contain duplicate values?
"""No, sets do not allow duplicate values. If you try to add a duplicate value, it will be ignored."""
duplicate_set = {1, 2, 3, 3, 4}
print(duplicate_set)  # Output: {1, 2, 3, 4}

# 🔹 12. How to perform set operations like union, intersection, difference, and symmetric difference?
"""Use the following methods:
- union(): Returns a new set with all unique elements from both sets.
- intersection(): Returns a new set with elements common to both sets.
- difference(): Returns a new set with elements in the first set but not in the second.
- symmetric_difference(): Returns a new set with elements in either set but not in both.
"""
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
print(setA.union(setB))              # Output: {1, 2, 3, 4, 5, 6}
print(setA.intersection(setB))       # Output: {3, 4}
print(setA.difference(setB))         # Output: {1, 2}
print(setA.symmetric_difference(setB))  # Output: {1, 2, 5, 6}

# 🔹 13. How to find the maximum and minimum values in a set?
"""Use the max() and min() functions."""
numbers = {1, 2, 3, 4, 5}
print(max(numbers))  # Output: 5
print(min(numbers))  # Output: 1

# 🔹 14. Can sets be nested within other sets?
"""No, sets cannot be nested within other sets because sets are mutable and not hashable. 
However, you can have a set of frozensets (which are immutable)."""
frozen_set = frozenset([1, 2, 3])
nested_set = {frozen_set}
print(nested_set)  # Output: {frozenset({1, 2, 3})}

# 🔹 15. How to convert a list to a set?
my_list = [1, 2, 3, 4, 5]
my_set = set(my_list)
print(my_set)  # Output: {1, 2, 3, 4, 5}

# 🔹 16. How to convert a set to a list?
my_list = list(my_set)
print(my_list)  # Output: [1, 2, 3, 4, 5]   

# 🔹 17. Can sets be used as dictionary keys?
"""No, sets cannot be used as dictionary keys because sets are mutable and not hashable."""
# Example
# my_dict = {my_set: "value"}  # This would raise a TypeError

# However, frozensets can be used as dictionary keys because they are immutable.
frozen_set = frozenset([1, 2, 3])
my_dict = {frozen_set: "value"}
print(my_dict)  # Output: {frozenset({1, 2, 3}): 'value'}

# 🔹 18. How to find the intersection of two sets?
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
intersection = setA.intersection(setB)
print(intersection)  # Output: {3, 4}

# 19 ⚠️ Empty set:
"""To create an empty set, using the set() constructor.
Using {} will create an empty dictionary, not a set."""
empty_set = set()
print(empty_set)  # Output: set()

# 🔹 20. Difference Between List and Set
"""
| Feature    | List      | Set           |
| ---------- | --------- | ------------- |
| Ordered    | ✅ Yes     | ❌ No          |
| Duplicates | ✅ Allowed | ❌ Not Allowed |
| Indexing   | ✅ Yes     | ❌ No          |
| Mutable    | ✅ Yes     | ✅ Yes         |

"""

# 🔹 21. How to Add Elements?
s = {1, 2}
s.add(3)
print(s) # Output: {1, 2, 3}

# Add multiple elements:
s.update([4, 5])
print(s) # Output: {1, 2, 3, 4, 5}

# 🔹 22. How to Remove Elements?
s = {1, 2, 3, 4, 5}
s.remove(2)   # Error if not found
s.discard(10) # No error
s.pop()       # Removes random element
s.clear()     # Removes all elements

# 🔹 23. Set Operations (Very Important)
a = {1, 2, 3}
b = {3, 4, 5}

# Union
print(a | b)  # Output: {1, 2, 3, 4, 5}

# Intersection
print(a & b)  # Output: {3}

# Difference
print(a - b)  # Output: {1, 2}

# Symmetric Difference
print(a ^ b)  # Output: {1, 2, 4, 5}

#🔹 24. What is FrozenSet?
"""
1. Immutable version of set
2. Cannot add/remove elements
3. Can be used as dictionary keys
4. Created using frozenset() function
"""
# OR
"""1. Immutable set
2. Cannot be modified after creation
3. Can be used as dictionary keys
4. Created using frozenset() function
"""
my_frozenset = frozenset([1, 2, 3]) 
print(my_frozenset)  # Output: frozenset({1, 2, 3})

# 🔹 25. Set Comprehension
squared_set = {x**2 for x in range(10)}
print(squared_set)  # Output: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}


# 🔹 26. What Are Subset and Superset?
a = {1, 2}
b = {1, 2, 3}

a.issubset(b)      # True
b.issuperset(a)    # True





#=====================================================================================================


# CHAPTER-10 : DICTIONARY IN PYTHON
