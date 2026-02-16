# What is list in python ?
"""A list is a built-in data type in Python used to store multiple values in a single variable.
Lists are ordered, mutable, and allow duplicate values."""

# OR

""" List is a collection of items that is ordered, mutable and allows dublicates elements. 
List can hold different data types such as integer, float, string boolean and None. """

#Example:
my_list = [1, 2, 3, 'Python',["Eshwar", "Adithya", "Rekha"]]
# fruits = ["apple", "banana", ]

# print(my_list)

# marks = [99, 97, 98.7, 96.45, 88.78]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(len(marks))
# print(sum(marks))
# print(sorted(marks))

# fruits = ["apple", "banana","cherry" ]
# fruits[0] = "Orange"
# print(fruits)

# fruits.append("grapes")
# fruits.insert(1, "Ananus")
# print(fruits)

# # Slicing
# print(fruits[1:4])

#----------------------------------------------

#List Methods
Cars = ["Maruthi", "Honda Suzuki", "Swift Dzire",]

# append :- Adds one element at the end of the list
Cars.append("BMW")
print(Cars)

Cars.sort()
print(Cars)
#------------------------------------------
# Sorted Ascending Order
num = [1, 5, 2, 0, 10, 3, 11 ,4]
num.sort()    # Sort in ascending order
print(num)

#-----------------------------------------------
# sorted Descending order
num.sort(reverse=True)  # Sort in Descending order
print(num)

#--------------------------------------------------
# Reverse List
num1 = [1, 5, 2, 0, 10, 3, 11 ,4]
num1.reverse()
print(num1)

#-----------------------------------------------------
# Insert element at index
cities = ["Bangalore", "Mysore", "Davanagere", "Hosapete"]
cities.insert(2, "Hubli")
print(cities)

cities.sort() # sort Ascending order
print(cities)

cities.sort(reverse=True)  # sort descending order
print(cities)


cities.append("Whitefield")
print(cities)
#----------------------------------------------------------