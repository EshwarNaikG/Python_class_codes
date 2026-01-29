# What is Tuple in python 
"""Tuple is a collection of items that is order and immutable."""
# OR
""" A tuple is a collection of items that is:
1. Ordered,
2. Immutable (cannot be changed),
3. Allows duplicate values, &
4. Can store multiple data types.
"""

#🔹 How to create a Tuple?
"""Using parentheses () with comma-separated values."""
# Example
my_tuple = (1, 2, 3, 'Python', ("Eshwar", "Adithya", "Rekha"))
print(my_tuple)

# 🔹 Creating a Tuple
a = ()                  # Empty tuple
b = (1, 2, 3)
c = tuple((4, 5, 6))     # Using tuple() constructor
print(a)
print(b)
print(c)

# 🔹 Creating a Tuple with Single Element
single_element_tuple = (10,)  # Note the comma
print(single_element_tuple)