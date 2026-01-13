# WAP to user's first name and print it's length.
str = input("Enter your first name : ")

print(f"length of name is: {len(str)}")

#----------------------------------------------
# WAP to find the occurrence of "$" in a string 
str1 = "Hi my $nmae i$ $Eshwar prce $1999"

print(str1.count("$"))

#---------------------------------------

# 🔹 Difference between strip(), lstrip(), rstrip()
"""
| Method     | Removes from |
| ---------- | ------------ |
| `strip()`  | Both sides   |
| `lstrip()` | Left side    |
| `rstrip()` | Right side   |

"""

# what is lstrip() ?
"""lstrip() Removes characters from the left side only"""
a = "abcpython"
print(a.lstrip("abc"))  # lstrip() Removes characters from the left side only

#----------------------------------------

# what is rstrip() ?
"""rstrip() Removes characters from the right side only"""
text = "Eshwar Naik"
print(text.rstrip("Naik"))  # rstrip() Removes characters from the right side only
