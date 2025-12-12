#1. Write a function to calculate the sum of two numbers
def calc_sum(a,b):
    sum =a + b
    print("Sum is:",sum)
    return sum
calc_sum(10,20)

#output: Sum is: 30

#OR
def calculate_sum(x, y):
    return x + y
result = calculate_sum(15, 25)
print("Sum is:", result)

#output: Sum is: 40

#--------------------------------------------------------------------------------------

#2. Write a function to check if a number is even or odd
def check_even_odd(num) :
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
    return
check_even_odd(15)

#3. Write a function to find the maximum of three numbers
def max_of_three(a,b,c):
    maximum = max(a,b,c)
    print("Maximum is:",maximum)
    return maximum
max_of_three(10,25,15)

#4. Write a function to reverse a string
def reverse_string(s):
    reversed_s = s[::-1]
    print("Reversed String is:",reversed_s)
    return reversed_s
reverse_string("Hello World")

#5. Write a function to check if a string is a palindrome
def is_palindrome(s):
    if s == s[::-1]:
        print(f'"{s}" is a Palindrome')
    else:
        print(f'"{s}" is not a Palindrome')
    return
is_palindrome("madam")

#output: "madam" is a Palindrome
#--------------------------------------------------------------------------------------


#6. Write a function to find the Fibonacci sequence up to n terms
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    print(f"Fibonacci sequence up to {n} terms:", fib_sequence)
    return fib_sequence
fibonacci(10)

#output: Fibonacci sequence up to 10 terms: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#--------------------------------------------------------------------------------------

#7. Write a function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F")
    return fahrenheit
celsius_to_fahrenheit(25)
#output: 25°C is equal to 77.0°F

#--------------------------------------------------------------------------------------

#8. Write a function to find the length of a string
def string_length(s):
    length = len(s)
    print(f"Length of the string '{s}' is:", length)
    return length
string_length("Hello World")
#output: Length of the string 'Hello World' is: 11

#--------------------------------------------------------------------------------------

#9. Write a function to calculate the area of a rectangle
def area_of_rectangle(length, width):
    area = length * width
    print(f"Area of rectangle with length {length} and width {width} is:", area)
    return area
area_of_rectangle(5, 10)

#output: Area of rectangle with length 5 and width 10 is: 50

#--------------------------------------------------------------------------------------

#10. Write a function to check if a number is prime
def is_prime(num):
    if num <= 1:
        print(f"{num} is not a Prime number")
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a Prime number")
            return False
    print(f"{num} is a Prime number")
    return True
is_prime(29)
#output: 29 is a Prime number
#--------------------------------------------------------------------------------------

#11. Write a function to find the GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    print(f"GCD is:", a)
    return a
gcd(48, 18)
#output: GCD is: 6

#---------------------------------------------------------------------------------------