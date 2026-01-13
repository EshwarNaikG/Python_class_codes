# Dictionary Methods:


student = {
    "name" : "Eshwar",
    "age" : 26,
    "marks" : {
        "phy" : 98,
        "chem" : 97,
        "maths" :100
    },
    "email" : "eshwar@gmail.com",
    "pwd" : "12345"
}
 # Meyhods
print(student.keys())  # returns all keys
print(student.values()) # returns all values
print(student.items()) # returns all (key, value) pairs as tuples
print(student.get("marks")) # returns the key according to value

# Inserts the specified items to the dictionary
print(student.update({"city" : "Bangalore", "birth place" : "Kogali Thanda", "course" : "Web developer"}))
print(len(student))
print(student)