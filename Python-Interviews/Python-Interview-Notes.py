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

