# 1️⃣ What is a dictionary in Python?
"""Dictionary is a built-in data type Python  used to store data in key : value pairs."""

# OR
"""Dictionary is a mutable, unordered collection of data that stores values in key : value pairs."""

# OR
"""A dictionary is a collection of key-value pairs where each key is unique and maps to a value.    
Dictionaries are mutable, unordered, and can store values of any data type."""

# 2️⃣ Key Features of a Dictionary
"""
✔ Stores data in key-value pairs
✔ Keys must be unique and immutable (e.g., strings, numbers, tuples)
✔ Values can be of any data type and can be duplicated
✔ Unordered (as of Python 3.7, they maintain insertion order)
✔ Mutable (you can add, remove, or change items)
"""
# OR
"""
1. Mutable (can be changed)

2. Stores data as key : value

3. Keys must be unique

4. Keys must be immutable (string, int, tuple)

5. Values can be any data type

6. Written using { } or dict() constructor
"""

# 3️⃣ Creating a Dictionary
# Using curly braces {}
my_dict = {
    "name": "Eshwar",
    "age": 30,
    "city": "Bangalore",
}
print(my_dict)  # Output: {'name': 'Eshwar', 'age': 30, 'city': 'Bangalore'}

# Using dict() constructor
my_dict2 = dict(name="Adithya", age=25, city="Mumbai")

print(my_dict2) # Output: {'name': 'Adithya', 'age': 25, 'city': 'Mumbai'}

# 4️⃣ Accessing Dictionary Values
my_dict = {
    "name": "Eshwar",
    "age": 30,
    "city": "Bangalore",
}
print(my_dict["name"])  # Output: Eshwar
print(my_dict.get("age"))  # Output: 30
print(my_dict.get("country", "Not Found"))  # Output: Not Found (default value)

# 5️⃣ Modifying a Dictionary
my_dict["age"] = 31  # Update existing key
print(my_dict)  # Output: {'name': 'Eshwar', 'age': 31, 'city': 'Bangalore'}
my_dict["country"] = "India"  # Add new key-value pair
print(my_dict)  # Output: {'name': 'Eshwar', 'age': 31, 'city': 'Bangalore', 'country': 'India'}

# 6️⃣ Deleting Items from a Dictionary
del my_dict["city"]  # Remove key-value pair by key
print(my_dict)  # Output: {'name': 'Eshwar', 'age': 31, 'country': 'India'}
my_dict.pop("age")  # Remove key-value pair and return value
print(my_dict)  # Output: {'name': 'Eshwar', 'country': 'India'}
my_dict.clear()  # Remove all items from the dictionary
print(my_dict)  # Output: {}

# 7️⃣ Dictionary Methods
my_dict = {
    "name": "Eshwar",
    "age": 30,
    "city": "Bangalore",
}
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])
print(my_dict.values())  # Output: dict_values(['Eshwar', 30, 'Bangalore'])
print(my_dict.items())  # Output: dict_items([('name', 'Eshwar'), ('age', 30), ('city', 'Bangalore')])  

# 8️⃣ Why use a Dictionary?
"""Dictionaries are ideal for storing and retrieving data based on unique keys.
They provide fast lookups and are useful for representing structured data, such as JSON objects."""

# 9️⃣ Dictionary Comprehension
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 10️⃣ Nested Dictionaries
nested_dict = {
    "person1": {"name": "Eshwar", "age": 30},
    "person2": {"name": "Adithya", "age": 25},
}

print(nested_dict) 
# Output: {'person1': {'name': 'Eshwar', 'age': 30}, 'person2': {'name': 'Adithya', 'age': 25}}

# 11️⃣ Dictionary vs List
"""| Feature           | Dictionary         | List              |
|-------------------|--------------------|-------------------|
| Data Structure    | Key-value pairs    | Ordered collection|
| Access            | By key             | By index          |
| Mutability        | Mutable            | Mutable           |
| Allows Duplicates | No (keys must be unique) | Yes               |
| Use Case          | When you need to associate values with unique keys | When you need an ordered collection of items |
"""
# How is a dictionary different from a list?
"""
| List                | Dictionary                      |
| ------------------- | ------------------------------- |
| Indexed by position | Indexed by keys                 |
| Allows duplicates   | Keys must be unique             |
| Ordered             | Insertion-ordered (Python 3.7+) |
| Access via index    | Access via key                  |
| When order matters or duplicates are needed | When you need to associate values with unique keys |
"""

# Dictionary Methods (Important)
"""
| Method     | Description             |
| ---------- | ----------------------- |
| `keys()`   | Returns all keys        |
| `values()` | Returns all values      |
| `items()`  | Returns key-value pairs |
| `get()`    | Get value safely        |
| `update()` | Update dictionary       |
| `copy()`   | Copy dictionary         |
| `clear()`  | Clear all items         |
"""

# Example-1
my_dict = {"name": "Eshwar", "age": 30, "city": "Bangalore"}
print(my_dict.keys())    # Output: dict_keys(['name', 'age', 'city'])
print(my_dict.values())  # Output: dict_values(['Eshwar', 30, 'Bangalore'])
print(my_dict.items())   # Output: dict_items([('name', 'Eshwar'), ('age', 30), ('city', 'Bangalore')])

# Looping Through Dictionary
student = {
    "name": "Eshwar",
    "age": 30,
    "city": "Bangalore",
}
for key in student:
    print(key, student[key])

for k, v in student.items():
    print(k, v)


#Nested Dictionary
# Example-1
students = {
    "student1": {"name": "Eshwar", "age": 30},
    "student2": {"name": "Adithya", "age": 25},
}
for student, details in students.items():
    print(student)
    for key, value in details.items():
        print(f"  {key}: {value}")

# Example-2
employees = {
    101: {"name": "Amit", "salary": 50000},
    102: {"name": "Sita", "salary": 60000}
}
for emp_id, emp_details in employees.items():
    print(f"Employee ID: {emp_id}")
    for key, value in emp_details.items():
        print(f"  {key}: {value}")

# Dictionary Comprehension
# Example-1: Create a dictionary of numbers and their squares
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Example-2: Create a dictionary from two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
combined_dict = {k: v for k, v in zip(keys, values)}
print(combined_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}    

# Example-3
# Create a dictionary of even numbers and their squares
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Check Key Exists
my_dict = {"name": "Eshwar", "age": 30, "city": "Bangalore"}
print("name" in my_dict)  # Output: True
print("country" in my_dict)  # Output: False

#Difference: [] vs get()

# Using [] to access a key that doesn't exist raises a KeyError,
#  while get() returns None (or a specified default value) without raising an error.
my_dict = {"name": "Eshwar", "age": 30, "city": "Bangalore"}
print(my_dict["name"])  # Output: Eshwar
print(my_dict.get("name"))  # Output: Eshwar
print(my_dict["country"])  # Raises KeyError
print(my_dict.get("country"))  # Output: None (doesn't raise KeyError)

# Example-2
student = {
    "name": "Eshwar",
    "age": 30,
    "city": "Bangalore",
}
student["marks"]   # ❌ KeyError
student.get("marks")  # ✅ None

# Dictionary vs List
"""
| Dictionary      | List          |
| --------------- | ------------- |
| key-value pairs | index-based   |
| unordered       | ordered       |
| fast lookup     | slower search |
| mutable         | mutable       |
"""

# Example-1
my_dict = {"name": "Eshwar", "age": 30, "city": "Bangalore"}
print(my_dict["name"])  # Output: Eshwar (fast lookup by key)

my_list = ["Eshwar", 30, "Bangalore"]
print(my_list[0]) 
# Output: Eshwar (access by index, slower search if you don't know the index)

# Real-World Example
# Example-1
# Storing student information in a dictionary
student_info = {
    "name": "Eshwar",
    "age": 30,
    "courses": ["Python", "Data Science"],
    "grades": {"Python": "A", "Data Science": "B+"}
}
print(student_info["name"])  # Output: Eshwar
print(student_info["courses"])  # Output: ['Python', 'Data Science']
print(student_info["grades"]["Python"])  # Output: A

# Example-2
login = {
    "username": "admin",
    "password": "1234"
}
print(login["username"])  # Output: admin

# Example-3
# Employees details
employees = {
    "name": "Eshwar",
    "Job" : "Python Developer",
    "Position": "Senior Developer",
    "Salary": 500000
}
print(employees)
print(employees("name"))  


