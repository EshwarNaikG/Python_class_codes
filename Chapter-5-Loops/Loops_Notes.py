# Chapter- LOOPS 
#What is loop in python ?
"""Loops are used to repeat a block of code multiple times."""
# Python supports:
"""
1. for loop

2. while loop

3. Nested loops

4. Loop control statements (break, continue, pass)
"""
#=========================================================================================

# cHAPTER - PYTHON FOR LOOP NOTES :-

# what is for loop in python?
"""
for loop is used to iterate over a sequence and execute a block of code
for each element.
"""
# OR
"""A for loop is used to iterate over a sequence and 
executes a block of code multiple times."""
#------------------------------------------------------------------
# ✅ 2. Basic Syntax
""" 
for variable in sequence:
    # code block
"""
#----------------------------------------------------------------
# ✅ 3. Loop with range()

# 1. 🔹 range(stop)
for i in range(5):
    print(i) 
# Output :- 0 1 2 3 4 
#-----------------------------------------------------------
# 2. 🔹 range(start, stop)
for i in range(2, 6):
    print(i)
# Output :- 2 3 4 5 
#--------------------------------------------------------------
# 3. 🔹 range(start, stop, step)
for i in range(1, 10, 2):
    print(i)
# Output :- 1 3 5 7 9 
#-------------------------------------------------------------------------------------------

# ✅ 4. Loop Through Different Data Types
# 🔹 List
nums = [10, 20, 30]
for n in nums:
    print(n)
#---------------------------------------------------------
# 🔹 String
for ch in "Python":
    print(ch)
#--------------------------------------------------------
# 🔹 Tuple
t = (1, 2, 3)
for i in t:
    print(i)
#------------------------------------------------------------
# 🔹 Set
s = {1, 2, 3}
for i in s:
    print(i)
#---------------------------------------------------
# 🔹 Dictionary
# 👉 Loop keys:
d = {"a":1, "b":2}
for key in d:
    print(key)

# 👉 Loop values:
for value in d.values():
    print(value)

# 👉 Loop key-value pairs:
for k, v in d.items():
    print(k, v)
#---------------------------------------------------------------------------------------

# ✅ 5. break Statement
"""Stops the loop immediately."""
for i in range(5):
    if i == 3:
        break
    print(i)
# Output :- 0 1 2
#-----------------------------------------------------------------------------------
# ✅ 6. continue Statement
"""Skips current iteration."""
for i in range(5):
    if i == 3:
        continue
    print(i)
# Output:- 0 1 2 4

#----------------------------------------------------------------------------------
# 7. for Loop with else
"""The else block executes when loop finishes normally (no break)"""
for i in range(3):
    print(i)
else:
    print("Completed")

#------------------------------------------------------------------------------------
# 8. Nested for Loop
"""Loop inside another loop."""
for i in range(3):
    for j in range(2):
        print(i, j)
# NOTES :-
"""Used in:

Pattern programs

Matrix operations

Tables"""
#--------------------------------------------------------------------------------------
# 9. Important Functions Used with for
# 🔹 enumerate()
"""Gives index + value"""
names = ["A", "B", "C"]

for index, value in enumerate(names):
    print(index, value)

#-------------------------------------------------------------------------------
# 🔹 zip()
"""Iterate multiple lists together"""
a = [1, 2, 3]
b = ["A", "B", "C"]

for x, y in zip(a, b):
    print(x, y)

#----------------------------------------------------------------------------
# 🔹 reversed()
for i in reversed(range(5)):
    print(i)

#--------------------------------------------------------------------------------------
# List Comprehension (Advanced Usage)
"""Shorter way to use loop"""
squares = [x*x for x in range(5)]
print(squares)

#========================================================================================

# CHAPTER-2 :- WHILE LOOP IN PYTHON

