# What is Tuple in python 
"""Tuple is a collection of items that is order and immutable."""


#---------------------------------------------

tuple = ()   # Create Empty Tuple
print(type(tuple))  

#----------------------------------------------

fruits = ("Apple",)  # Create Tuple with single value
print(fruits)
print(type(fruits))

#--------------------------------------------------------

num = (1, 2, 3, "Naik", 4, 5, 6, 7, 8, 9, 10)  # Tuples with multiple values
print(num)
print(type(num))

#slicing
print(num[1:5])
print(num[0:3])
print(num[-1])
print(num[:-1])
print(num[::2])
print(num.index("Naik"))

#---------------------------------------------------------

# Tuples Methods:
# index method
names = ("Eshwar", "Adithya", "Rekha","Kanchana","Yash", "Eshwar", "Eshwar")
print(names.index("Rekha"))
print(names.index("Eshwar"))

# count method
print(names.count("Eshwar"))
