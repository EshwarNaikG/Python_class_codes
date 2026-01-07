# What is conditional statement in Python ?
"""A conditional statement is used to perform decision-making.
It executes different code blocks based on whether a given condition is True or False.""" 

# OR

""" Conditional statement  executes different code blocks 
based on whether a given condition is True or False. """


#---------------------------------------------------------------------
# if-elif-else (syntax)

"""
if (condition):
    statement1

elif (condition):
    statement2

else:
    statement3
"""

#------------------------------------------------------------------------
# Examples-1:

# age = 21
# if(age>=18):
#     print("You are Eligible for vote")

#-------------------------------------
#Example-2
# light = "green"
# if(light=="red"):
#     print("Stop")

# elif(light=="yellow"):
#     print("Look")

# elif(light=="green"):
#     print("Go")

# else:
#     print("Invalid Color selection!")

#---------------------------------------------
#Example-3
# light1 = input("Enter your color : ")
# if(light1=="red"):
#     print("Stop")

# elif(light1=="yellow"):
#     print("Look")

# elif(light1=="green"):
#     print("Go")

# else:
#     print("Invalid Color selection!")

#-------------------------------------------------
# Example-4 : Calculator- user input values

# n1 = int(input("Enter your first number : "))
# n2 = int(input("Enter your second number : "))
# op = input("Enter your operator : (+, -, *, /, **, %, //) : ")

# if(op == "+"):
#     print(n1+n2)

# elif(op =="-"):
#     print(n1-n2)

# elif(op =="*"):
#     print(n1*n2)

# elif(op =="/"):
#     print(n1/n2)

# elif(op =="**"):
#     print(n1**n2)
# elif(op =="%"):
#     print(n1%n2)

# elif(op =="//"):
#     print(n1-n2)

# else:
#     print("Your select invalid operators")


#--------------------------------------------------------
# Example-5
# Find given number is even or odd

# num = int(input("Enter your number : "))

# if(num % 2 == 0):
#     print(f"Given number {num} is even number")

# else:
#     print(f"Given number {num} is odd number")

#-------------------------------------------------------------
# Find greatest number

# num1 = int(input("Enter your first number : "))
# num2 = int(input("Enter your second number : "))
# num3 = int(input("Enter your third number : "))

# if(num1 >= num2 and num1 >= num3):
#     print("First is greatest number")

# elif( num2 >= num3 ):
#     print("Second number is greatest number")

# else:
#     print("Third number is greatest number")

#------------------------------------------------------------

# WAP to check if a number is multiple of 7 or not

a = int(input("Enter your numbes: "))
if(a % 7 == 0):
    print(f"The given number {a} is multiple of 7 ")
else:
    print(f"The given number {a} is not multiple of 7 ")

 #--------------------------------------------------------------------   
