# What is Type conversion in pthon ?  Automatically changing
"""Type conversion is the process of changing one data type into another data type
to make operations possible in Python."""


# Examples

a = 2    # int
b = 4.5  # float
sum = a + b  # 2.0 + 4.5 = 6.5
print(sum)

#----------------------------------------

n1 = 10   #int
# n2 = "20" # string
# add = n1 + n2   #TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(add)  # Error


# Type Casting :
n2 = int(20)

add = n1 + n2
print(add)