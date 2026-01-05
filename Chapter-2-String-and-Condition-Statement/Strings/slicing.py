# What is slicing in Python ?
"""in Python Slicing is extracts a portion of a string using start, end, and step values."""

"""OR"""

"""Slicing is accessing a parts a string."""

# Difference: Indexing vs Slicing
"""
   Indexing	                      Slicing
Returns one character	       Returns multiple characters
Uses single index	           Uses range
Example: s[2]	               Example: s[1:4]

"""


"""
string[start : end : step]

start → starting index (inclusive)

end → ending index (exclusive)

step → increment (optional)
"""

#----------------------------------------------------
# Examples :
text = "Python"

print(text[0:4])   # Pyth
print(text[2:])    # thon
print(text[:3])    # Pyt
print(text[-4:-1]) # tho

#------------------------------------------------------

# Examples-2
text = "Python"

print(text[::2])   # Pto
print(text[::-1])  # nohtyP (reverse string)

#-------------------------------------------------
# REVERSE STRING : IMPORTANT
name = "Eshwara Naik G"
print(name[::-1])
