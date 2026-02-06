# What is set in python ?
"""A set is a collection of unique elements that is unordered, mutable (can be changed)
and do not allow duplicate values.
"""
# OR
"""A set is an unordered, mutable collection of unique elements."""
# ✅ Key Features of a Set
"""
✔ Stores only unique values (no duplicates)
✔ Unordered (no indexing or slicing)
✔ Mutable (you can add or remove elements)
✔ Written using curly braces {} or set() function
"""
#OR
"""
1. ✅ Stores unique values only

2. ❌ No indexing (no set[0])

3. 🔄 Unordered

4. ✏️ Mutable (can add/remove items)

5. ⚡ Faster membership testing than lists
"""
#----------------------------------------------------------------------------------------   
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
#---------------------------------------------------------------------
# Common Set Operations :
#Add elements-1
s = {1, 2}
s.add(3)
print(s)  # Output: {1, 2, 3}
#-------------------------------------------------------------------------------    

# 🔹 Creating a Set
null_set = set()      # Empty set
print(type(null_set)) # <class 'set'>

s1 = {10, 20, 30}
s2 = set([1, 2, 3])
s3 = set()        # empty set (NOT {})
print(s1)
print(s2)
print(s3)

# NOTE: {} creates an empty dictionary, not a set.
# To create an empty set, use the set() function.

#--------------------------------------------------------------------------------
# 🔹 Duplicate Values Removed Automatically

# Example-1
set1 = {1, 1, 2, 2, 3, 3, 4, 4}
print(set1)   # Set do not allow duplicate values.  
# Output: {1, 2, 3, 4}


# Example-2
collection = {1, 2, 3, 3, "eshwar", "eshwar", "hello", "hello", "world", "world" ,4, 5}
print(collection) # Output: {1, 2, 3, 4, 5, 'eshwar', 'hello', 'world'}
print(len(collection))  # Total number of items. Dupliates are not allowed
# Output: 8


# Example-3
fruits = {"apple", "banana", "cherry", "apple", "banana"}
print(fruits)  # Output: {'banana', 'cherry', 'apple'}
print(len(fruits))  # Output: 3. Duplicates are removed automatically.
#-----------------------------------------------------------------------------------------

# 🔹 Accessing Set Elements
""" 
1. Sets are unordered, so you cannot access elements by index.
2. However, you can iterate through the set using a for loop.
"""
# You cannot access by index. Use a loop:

# Example-1
my_set = {1, 2, 3, 'Python', 'Eshwar'}
for item in my_set:
    print(item)

# Example-2
colors = {"red", "green", "blue"}
for color in colors:
    print(color)  # Output: red green blue (order may vary)

# -----------------------------------------------------------------------------------------

# 🔹 Common Set Operations :

# Check membership............................................
my_set = {1, 2, 3, 'Python', 'Eshwar'}
print(2 in my_set)        # True
print('Java' in my_set)   # False

# 🔹 Adding Elements..........................................
s = {1, 2}
s.add(3)
print(s)  # Output: {1, 2, 3}
s.update([4, 5])
print(s)  # Output: {1, 2, 3, 4, 5}

# 🔹 Removing Elements..........................................
s = {1, 2, 3, 4}
s.remove(3)   # error if element not found
s.discard(4)  # no error if not found
s.pop()       # removes random element
s.clear()     # removes all elements
print(s)       # Output: set() , after clear

#-------------------------------------------------------------------------------------------------

# 🔹 Set Methods (Quick List)
"""
| Method         | Description    |
| -------------- | -------------- |
| add()          | Add element    |
| update()       | Add multiple   |
| remove()       | Remove element |
| discard()      | Remove safely  |
| pop()          | Remove random  |
| clear()        | Empty set      |
| union()        | Combine sets   |
| intersection() | Common values  |
| difference()   | A − B          |
| issubset()     | Check subset   |
| issuperset()   | Check superset |

"""

#----------------------------------------------------------------------------------------------------

# 🔹 Set Operations: Union, Intersection, Difference........................

# Union................................
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # Output: {1, 2, 3, 4, 5} (union)
print(a.union(b))  # Output: {1, 2, 3, 4, 5} (union method)

# Intersection..............................
print(a & b)  # Output: {3} (intersection)
print(a.intersection(b))  # Output: {3} (intersection method)

# Difference..................................
print(a - b)  # Output: {1, 2} (difference)
print(a.difference(b))  # Output: {1, 2} (difference method)

# Symmetric Difference..........................
print(a ^ b)  # Output: {1, 2, 4, 5} (symmetric difference)
print(a.symmetric_difference(b))  # Output: {1, 2, 4, 5} (symmetric difference method)


# 🔹 Example
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)   # {1, 2, 3, 4, 5}, Union
print(A & B)   # {3}, Intersection
print(A - B)   # {1, 2}, Difference
print(A ^ B)   # {1, 2, 4, 5}, Symmetric Difference 


#--------------------------------------------------------------------------------------------------
# 🔹 Set Comparison: Subset and Superset...............................
A = {1, 2}
B = {1, 2, 3, 4, 5}
print(A.issubset(B))    # True
print(B.issuperset(A))  # True

# Example-2
setA = {10, 20}
setB = {10, 20, 30, 40, 50}
print(setA.issubset(setB))    # True
print(setB.issuperset(setA))  # True

# Example-3
fruitsA = {"apple", "banana"}
fruitsB = {"apple", "banana", "cherry", "date"}
print(fruitsA.issubset(fruitsB))    # True  
print(fruitsB.issuperset(fruitsA))  # True
#--------------------------------------------------------------------------------------------------

# 🔹 Set Operations Summary Table..............................
"""
| Operation            | Symbol/Method            | Description                          |
| -------------------- | ------------------------ | ------------------------------------ |
| Union                | a | b or a.union(b)       | Combines elements from both sets     |
| Intersection         | a & b or a.intersection(b)| Elements common to both sets         |
| Difference           | a - b or a.difference(b)| Elements in a but not in b           |
| Symmetric Difference | a ^ b or a.symmetric_difference(b)| Elements in either set but not both |
| Subset Check         | a.issubset(b)           | Checks if a is a subset of b         |
| Superset Check       | a.issuperset(b)         | Checks if a is a superset of b       |
"""

#------------------------------------------------------------------------------------------------

# 🔹 Set vs List (Interview Favorite)
"""
| Feature          | Set    | List      |
| ---------------- | ------ | --------- |
| Duplicate values | ❌ No   | ✅ Yes     |
| Order            | ❌ No   | ✅ Yes     |
| Mutable          | ✅ Yes  | ✅ Yes     |
| Indexing         | ❌ No   | ✅ Yes     |
| Speed            | ⚡ Fast | 🐢 Slower |

"""

#----------------------------------------------------------------------------------------------
# 🔹 When to Use Set?
"""
1. Remove duplicates

2. Membership testing (in)

3. Mathematical set operations

4. Comparing collections
"""