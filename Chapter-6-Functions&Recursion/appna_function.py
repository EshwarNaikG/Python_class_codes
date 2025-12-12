# Practice
# 1.Write a functio to print the length of a list
cities =["Bangalore", "Mumbai", "Chennai", "Kolkata", "Delhi"]
heroes = ["Superman", "Batman", "Wonder", "Eshwar","Adithya","Darshan"]

def print_length(list):
    print("Length of the list is:", len(list))
print_length(cities)
print_length(heroes)

#output:
#Length of the list is: 5
#Length of the list is: 6

# 2.Write a function to print all the items in a list

def print_list(list):
    for item in list:
        print(item, end=" ")
print_list(cities)
print()  # for newline
print_list(heroes)  

#output:
#Bangalore Mumbai Chennai Kolkata Delhi
#Superman Batman Wonder Eshwar Adithya Darshan

####################################################################################################

# 3.Write a function to find the maximum number in a list of numbers
numbers = [34, 67, 23, 89, 12, 90, 45]
def find_maximum(num_list):
    maximum = max(num_list)
    print("Maximum number in the list is:", maximum)
    return maximum
find_maximum(numbers)


#-----------------------------------------------------------------------------------------------

#4. WAF to find the factorial of n. (n is the parameter to the function)

def find_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(f"Factorial of {n} is:", fact)
    return fact
find_factorial(5)
find_factorial(7)

# OR
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)
# Calling the function
print("Factorial of 6 is",fact(6))  # Output: 720

#-----------------------------------------------------------------------------------------------

# 5. WAF to convert USD to INR. (Assume 1 USD = 83 INR)
def converter(usd_val):
    inr_val = usd_val * 83
    print(f"{usd_val} USD is equal to {inr_val} INR")
    return inr_val
converter(100)
converter(250)
converter(73)

#-----------------------------------------------------------------------------------------------
# 6. WAF to check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
    return
check_even_odd(42)
check_even_odd(77)