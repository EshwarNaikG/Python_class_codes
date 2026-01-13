# What is Identity in Python?
"""Identity in Python refers to whether two variables point to the same object in memory."""

# Checking memory location of different objects

# Example-1:
a = 100
b = 100
print(id(a))
print(id(b))

#-------------------------------
# Example-2
a = 10
b = 10
c = 10
print(id(a)) # memory location : same because variable points to the same object 
print(id(b)) # memory location : same because variable points to the same object 
print(id(c)) # memory location : same because variable points to the same object 

#--------------------------------------

# Example-3
# Memory location of mutable objects
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(id(list1)) #different addresses
print(id(list2)) # different addresses
