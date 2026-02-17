# Find and calculate square root of given numbers
# Solution-1 :- Using Exponention

n = int(input("Enter your numbers : "))
sqr = n ** (1/2)
print(f"The square root of given number is {sqr}")

#----------------------------------------------------------------------------------------------

# Solution-2 : Using math module

import math
num = int(input("Enter your numbers : "))
sq = math.sqrt(num)
print(f"The square root of given number is {sq}")