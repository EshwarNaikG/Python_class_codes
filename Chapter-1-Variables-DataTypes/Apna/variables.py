# What is variable in python ?
"""Variable is a container used to stored  different types of values"""
"""OR"""
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

#practical"
a =10    # int
print(a)
print(type(a))

#---------------------------

b = 12.5    # float
print(b)
print(type(b))

#-----------------------------
c = 12+5j    # complex
print(c)
print(type(c))

#----------------------------
d = True
print(d)
print(type(d))

#--------------------------------
list1 = [10, "eshwar", 2+5j, 5.7, True, False, (1,2,3)]   # List
print(list1)
print(type(list1))

#--------------------------------
x = 5
y = x
x=10
print(y)