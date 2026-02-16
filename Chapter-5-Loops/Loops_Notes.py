# cHAPTER - PYTHON FOR LOOP NOTES :-

# what is for loop in python?
"""
for loop is used to iterate over a sequence and execute a block of code
for each element.
"""
# OR
"""A for loop is used to iterate over a sequence and 
executes a block of code multiple times."""

# ✅ 2. Basic Syntax
""" 
for variable in sequence:
    # code block
"""

# ✅ 3. Loop with range()

# 1. 🔹 range(stop)
for i in range(5):
    print(i) 
# Output :- 0 1 2 3 4 

# 2. 🔹 range(start, stop)
for i in range(2, 6):
    print(i)
# Output :- 2 3 4 5 

# 3. 🔹 range(start, stop, step)
for i in range(1, 10, 2):
    print(i)

# Output :- 1 3 5 7 9 

