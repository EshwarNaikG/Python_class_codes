# What is set in python ?
"""A set is a collection of unique elements that is unordered and mutable (can be changed).
Set do not allow duplicate values.
"""

# ✅ Key Features of a Set
"""
✔ Stores only unique values (no duplicates)

✔ Unordered (no indexing or slicing)

✔ Mutable (you can add or remove elements)

✔ Written using curly braces {} or set() function
"""


null_set = set()      # Empty set
print(type(null_set)) # <class 'set'>
#---------------------------------------------------------------------
# Examples-1
my_set = {1, 2, 3, 4}
print(my_set)

#------------------------------------------------------------------
#Examples-2
#Duplicate Values Are Not Allowed
set1 = {1, 1, 2, 2, 3, 3, 4, 4}
print(set1)   # Set do not allow duplicate values.

#-----------
collection = {1, 2, 3, 3, "eshwar", "eshwar", "hello", "hello", "world", "world" ,4, 5}
print(collection)
print(len(collection))  # Total number of items. Dupliates are not allowed

#------------------------------------------------------------------------
# Common Set Operations :

#Add elements-1
s = {1, 2}
s.add(3)
print(s)
#------------------------------------------
# Remove elements
set2 = {1, 1, 2, 2, 3, 3, 4, 4}
set2.remove(4)
print(set2)

# set2.remove(5)  # error if element not found
set2.discard(5)  # no error
print(set2)

#------------------------------------------------
# Union, Intersection, Difference
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # Union: {1, 2, 3, 4,5}
print(a & b)   # Intersection: {3}
print(a - b)   # Difference : {1, 2}

#--------------------------------------------------

set1 = {1, 2, 3}
set2 = {3, 4, 5}

set3 = set1.union(set2)   # {1, 2, 3, 4, 5}
print(set3)
# OR
print(set1.union(set2))  # {1, 2, 3, 4, 5}
#--------------------------
set3 = set1.intersection(set2) # {3}
print(set3)
# OR
print(set1.intersection(set2)) # {3}

#-----------------------------------------------------------------
