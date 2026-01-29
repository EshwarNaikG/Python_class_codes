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