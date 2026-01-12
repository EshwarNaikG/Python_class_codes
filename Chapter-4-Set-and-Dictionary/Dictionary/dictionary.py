# Dictionary in python 
"""Dictionaries are used to store data values in key:value pairs.
They are unordered, mutable(changeble) and don't allow duplicate keys."""

# Example-1
dict = {
    "name" : "Eshwar",
    "age": 32,
    "is_Adult" : True,
    "email" : "eshwarnaik79@gmail.com",
    "city" : "Bangalore",
    "marks" : [99, 94, 98.9, 95.7]    # list in dictionary
}

print(dict)


# Example-2
karnataka_food = {
    "Davanagere"  : "Benne Dose",
    "Mysore" : "Mysore Pak",
    "Bangalore" : "Bisibele Bath",
    "Mandya" : "Ragi mudde"
}

print(karnataka_food)

karnataka_food["shivamogga"] = "Palav"  # add items
print(karnataka_food)

