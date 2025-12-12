# what is for loop in python?




# Example of for loop in python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry
#--------------------------------------------------------------------------------------------   
# Example of for loop with range()
for i in range(5):
    print(i)

#--------------------------------------------------------------------------------------------
# Example of for loop with break statement
for i in range(10):
    if i == 5:
        break
    print(i)


#--------------------------------------------------------------------------------------------
# Example of for loop with continue statement
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

#--------------------------------------------------------------------------------------------
# Example of nested for loop
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

#--------------------------------------------------------------------------------------------
# Example of for loop with else statement
for i in range(5):
    print(i)
else:
    print("Loop completed")

#--------------------------------------------------------------------------------------------
# Example of iterating over a dictionary
person = {"name": "Eshwar", "age": 21, "city": "Bangalore"}
for key, value in person.items():
    print(f"{key}: {value}")

#--------------------------------------------------------------------------------------------
# Example of using enumerate() in for loop
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Index: {index}, Color: {color}")    

#--------------------------------------------------------------------------------------------
# Example of using zip() in for loop
names = ["Eshwar", "Adithya", "Rohan"]
ages = [21, 22, 20]
for name, age in zip(names, ages):
    print(f"Name: {name}, Age: {age}")

#--------------------------------------------------------------------------------------------
# Example of using list comprehension with for loop
squares = [x**2 for x in range(10)]
print(squares)

# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#--------------------------------------------------------------------------------------------

