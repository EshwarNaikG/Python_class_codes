# # What is Function in Python?
"""A function is a block of reusable code that performs a specific task."""

"""
✔ Improves code reusability
✔ Makes program modular
✔ Reduces repetition
"""

# 1️⃣ Defining a Function
# 🔹 Syntax
"""
def function_name(parameters):
    # block of code
    return value

"""

# 2️⃣ Simple Function Example
# Example-1
def greet():
    print("Hello, Eshwar")

greet()

"""
✔ def → keyword to define function
✔ greet() → function call
"""

# 3️⃣ Function with Parameters
def greet(name):
    print("Hello", name)

greet("Eshwar")


# 4️⃣ Function with Return Value
def add(a, b):
    return a + b

result = add(10, 20)
print(result)

"""
✔ return sends value back to caller
✔ Without return, function returns None
"""

# 5️⃣ Types of Function Arguments

# 🔹 1. Positional Arguments
def add(a, b):
    return a + b

add(10, 20)

# 🔹 2. Keyword Arguments
add(a=10, b=20)


# 🔹 3. Default Arguments

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Eshwar")

# 🔹 4. Variable-Length Arguments

# *args (Multiple positional arguments)
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3, 4))


# **kwargs (Multiple keyword arguments)
def details(**data):
    print(data)

details(name="Eshwar", age=22)

# 6️⃣ Types of Functions :-

#🔹 1. Built-in Functions
"""
print()
len()
type()
sum()
"""

# 🔹 2. User-defined Functions
"""Functions created using def"""

# 🔹 3. Lambda Function (Anonymous Function)
square = lambda x: x * x
print(square(5))


# 7️⃣ Recursive Function
"""Function calling itself."""
# Example-1 :- Factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

"""
✔ Must have base condition
✔ Otherwise infinite recursion
"""

# 8️⃣ Local vs Global Variables:-

x = 10   # Global

def test():
    y = 5   # Local
    print(x, y)

test()

"""
✔ Local variable exists only inside function
✔ Global variable exists everywhere
"""

# To modify global variable:
x = 10

def change():
    global x
    x = 20

# 9️⃣ Function with pass 
def my_function():
    pass

"""Used as placeholder."""


# 🔟 Docstring (Function Documentation)
def add(a, b):
    """This function returns sum of two numbers"""
    return a + b
# Access using:
print(add.__doc__)


# 🎯 Interview Points
"""
✔ What is difference between parameter and argument?
✔ What is default argument?
✔ What is recursion?
✔ What is lambda function?
✔ Difference between local and global variable?
✔ What happens if function has no return?
"""

# 🚀 Advanced Topics (Important for Interviews)
"""
1. First-class functions
2. Higher-order functions
3. Decorators
4. Closures
5. Function annotations
6. Map, filter, reduce
"""






