# What is Tuple in python ?.......................................................................
"""Tuple is a collection of items that is order and immutable, allow duplicate values 
and can store multiple data types."""
# OR
""" A tuple is a collection of items that is:
1. Ordered,
2. Immutable (cannot be changed),
3. Allows duplicate values, &
4. Can store multiple data types.
"""

#🔹 How to create a Tuple?........................................................................
"""Using parentheses () with comma-separated values."""
# Example
my_tuple = (1, 2, 3, 'Python', ("Eshwar", "Adithya", "Rekha"))
print(my_tuple)

# 🔹 Creating a Tuple..................................................................................
a = ()                  # Empty tuple
b = (1, 2, 3)
c = tuple((4, 5, 6))     # Using tuple() constructor
print(a)
print(b)
print(c)

# 🔹 Creating a Tuple with Single Element
single_element_tuple = (10,)  # Note the comma
print(single_element_tuple)

# 🔹 Accessing Tuple Elements
my_tuple = (1, 2, 3,3, 'Python', ("Eshwar", "Adithya", "Rekha"))
print(my_tuple[0])      # First element
print(my_tuple[-1])     # Last element
print(my_tuple[3])      # Fourth element
print(my_tuple[4][0])   # First element of nested tuple 

#🔹 Characteristics of Tuple..........................................................................
"""
| Feature           | Tuple |
| ----------------- | ----- |
| Ordered           | ✅     |
| Indexed           | ✅     |
| Mutable           | ❌     |
| Allows duplicates | ✅     |
| Faster than list  | ✅     |

"""
# 🔹 Why use Tuple over List?..................................................................
"""Tuples are immutable, so they are safer for data that should not change. 
They are also faster than lists and can be used as dictionary keys (since they are immutable)."""

# ✅ Single element tuple..........................................................................
single_element = (42,) # Note the comma is mandatory
print(type(single_element))  # Output: <class 'tuple'>

# ❌ Not a tuple, just an integer in parentheses
not_a_tuple = (42)
print(type(not_a_tuple))  # Output: <class 'int'>

t = (10)    # int, not tuple

# 🔹 Accessing Tuple Elements (Indexing)..............................................................
# Example-1
my_tuple = (1, 2, 3,3, 'Python', ("Eshwar", "Adithya", "Rekha"))
print(my_tuple[0])      # First element
print(my_tuple[-1])     # Last element
print(my_tuple[3])      # Fourth element
print(my_tuple[4][0])   # First element of nested tuple 

#example-2
colors = ("Red", "Green", "Blue", "Yellow")
print(colors[1])  # Output: Green
print(colors[-2]) # Output: Blue    

# Example-3
t = (10, 20, 30, 40)
print(t[0])     # 10
print(t[-1])    # 40

# 🔹 Tuple Slicing...........................................................
# Example-1
t = (10, 20, 30, 40, 50)
print(t[1:4])   # (20, 30, 40)
print(t[:3])    # (10, 20, 30)

# Example-2
fruits = ("Apple", "Banana", "Cherry", "Date", "Elderberry")
print(fruits[1:4])  # Output: ('Banana', 'Cherry', 'Date')
print(fruits[:3])   # Output: ('Apple', 'Banana', 'Cherry')
print(fruits[2:])   # Output: ('Cherry', 'Date', 'Elderberry')

# Example-3
t = (10, 20, 30, 40, 50, 60)
print(t[2:5])   # (30, 40, 50)
print(t[:4])    # (10, 20, 30, 40)
print(t[3:])    # (40, 50, 60)


# 🔹 Tuple Immutability.........................................................................
"""Tuples are immutable, meaning their elements cannot be changed after creation."""

"""❌ Cannot modify:"""
# Example-1
t = (10, 20, 30)
t[1] = 99   # TypeError

# Example
t = (10, 20, 30)
# t[0] = 100  # This would raise an error: TypeError: 'tuple' object does not support item assignment

# Example-2
t = (10, 20, 30)
t[1] = 99   # TypeError
# This will raise an error because tuples are immutable

# 🔹 Looping Through Tuple...............................................................................
# Example-1
t = (10, 20, 30, 40)
for i in t:
    print(i)

# Example-2
fruits = ("Apple", "Banana", "Cherry")
for fruit in fruits:
    print(fruit)

#Using index:......................................................................................
# Example-3
t = (10, 20, 30, 40)
for i in range(len(t)):
    print(t[i])


# 🔹 Tuple Functions (Built-in).................................................................
t = (10, 20, 30, 20)

print(len(t))      # 4
print(max(t))      # 30
print(min(t))      # 10
print(sum(t))      # 80
print(sorted(t))   # [10, 20, 20, 30]


# 🔹 Tuple Methods........................................................................................
# count() - Returns the number of occurrences of a value
t = (10, 20, 30, 40, 50, 60)
print(t.count(10))  # Output: 1

# index() - Returns the index of the first occurrence of a value
print(t.index(30))  # Output: 2

# 🔹 Tuple Methods (Only 2).........................................................................
"""Tuples have only two built-in methods: count() and index()."""
# Example-1
t = (10, 20, 30, 20)

print(t.count(20))   # 2
print(t.index(30))   # 2

# Example-2
grades = ( "A", "B", "A", "C", "B", "A" )
print(grades.count("A"))  # Output: 3

print(grades.index("C"))  # Output: 3



# 🔹 Tuple Packing & Unpacking...........................................................................
# Tuple Packing
packed_tuple = 1, 2, 3, "Hello"
print(packed_tuple)  # Output: (1, 2, 3, 'Hello')

# Tuple Unpacking
a, b, c, d = packed_tuple
print(a, b, c, d)  # Output: 1 2 3 Hello

# 🔹 Swapping Using Tuple.................................................................................
a = 10
b = 20

a, b = b, a
print(a, b)
# Output: 20 10

# Example-2
x = "Apple"
y = "Banana"
x, y = y, x
print(x, y)  # Output: Banana Apple

# Example-3
m = 5   
n = 10
m, n = n, m
print(m, n)  # Output: 10 5

# 🔹 Nested Tuple.................................................................................
# Example-1
nested_tuple = (1, 2, (3, 4), (5, 6))
print(nested_tuple[2])      # Output: (3, 4)
print(nested_tuple[2][0])   # Output: 3

# Example-2
nested = ( "A", "B", ("C", "D"), ("E", "F") )
print(nested[2])        # Output: ('C', 'D')
print(nested[2][1])     # Output: D


#🔹 Tuple vs List........................................................................................
"""Tuples are immutable and generally faster, while lists are mutable and more flexible."""

"""
| Feature      | **List**                                | **Tuple**                         |
| ------------ | --------------------------------------- | --------------------------------- |
| Syntax       | `[ ]` square brackets                   | `( )` parentheses                 |
| Mutability   | ✅ Mutable (can change)                 | ❌ Immutable (cannot change)     |
| Performance  | Slower                                  | Faster                            |
| Memory Usage | More                                    | Less                              |
| Methods      | Many methods (`append`, `remove`, etc.) | Few methods (`count`, `index`)    |
| Use Case     | When data changes                       | When data is fixed                |
| Hashable     | ❌ No                                  | ✅ Yes (if elements are immutable)|

"""
# Example-1 
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
print(type(my_list))   # <class 'list'>
print(type(my_tuple))  # <class 'tuple'>

# Example-2
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_list[0] = 10        # Valid
# my_tuple[0] = 10     # Invalid, raises TypeError  

# Example-3
import sys
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
print(sys.getsizeof(my_list))   # Size of list
print(sys.getsizeof(my_tuple))  # Size of tuple

# Example-4
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
print(dir(my_list))    # List methods
print(dir(my_tuple))   # Tuple methods

# 🔹 When to use Tuple over List?.................................................................
"""Tuple uses when the data should not change, for fixed collections of items,
 or when you need to use the collection as a dictionary key."""

# OR
""" Tuples uses for fixed collections of items that should not change throughout the program."""

# Q: Why tuple is faster than list?
"""👉 Because tuples are immutable and have a fixed memory allocation."""
