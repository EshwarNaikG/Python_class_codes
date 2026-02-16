# What is Type casting in Python ?
"""Type casting is the manual conversion of one data type into another data type
 using Python’s built-in functions."""

# Examples

a = 4
b = "7.8"
c = float(b)
sum = a + c
print(sum)

#----------------------------------

# Note:-  User input values always return in string.

n1 = int(input("Enter first number : "))   # converting string into integer# 
n2 = int(input("Enter second number : "))  # converting string into integer# 

mult = n1 * n2
print(f"Multiflication of {n1} & {n2} is : {mult}")

#---------------------------------

num = 34.71     # folat
print(type(num)) #<class 'float'>
num2 = str(num)   # converting float into string
print(num2)
print(type(num2)) # <class 'str'>

#------------------------------------