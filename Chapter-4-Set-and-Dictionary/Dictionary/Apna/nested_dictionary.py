# Nested Dictionary

student = {
    "name" : "Eshwar",
    "subjects" : {            # nested dictionary
        "maths" : 99,
        "chem" : 98.7,
        "phys" :97,
        "Bioalogy" : 96.6
    },
    "surname" : "Naik",
    "age" : 32,
    "cell_number" : "7483529142"
}

print(student)
print(student["subjects"])
print(student["subjects"] ["chem"])

print(student.keys())

print(list(student.keys()))