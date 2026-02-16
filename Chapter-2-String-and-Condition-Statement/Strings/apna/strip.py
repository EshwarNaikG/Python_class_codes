# What is strip() ?
"strip() method removes characters or spaces from both sides"
# Example:
a = "   hello, world!    "
print(a)
print(a.strip(" ")) # strip() method removes characters or spaces from both sides

#---------------------------------------------------------------------

# what is lstrip() ?
"""lstrip() Removes characters or spaces from the left side only"""
a = "abcpython"
print(a.lstrip("abc"))  # lstrip() Removes characters from the left side only

#----------------------------------------

# what is rstrip() ?
"""rstrip() Removes characters or spaces from the right side only"""
text = "Eshwar Naik"
print(text.rstrip("Naik"))  # rstrip() Removes characters from the right side only


# 🔹 Difference between strip(), lstrip(), rstrip()
"""
| Method     | Removes from |
| ---------- | ------------ |
| `strip()`  | Both sides   |
| `lstrip()` | Left side    |
| `rstrip()` | Right side   |

"""