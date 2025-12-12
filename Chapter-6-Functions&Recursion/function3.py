#Function to multiply two numbers and print the result

def mult(a,b) :
    m = a*b
    print(f"Multiplication of  {a} and {b} is:", m)
    return m
mult(5,4)
mult(7,8)
mult(10,3)
mult(6,9)
#output:
#Multiplication of  5 and 4 is: 20  
#Multiplication of  7 and 8 is: 56
#Multiplication of  10 and 3 is: 30
#Multiplication of  6 and 9 is: 54


##################################################################################

#Function to calculate the power of a number
def power(base,exponent):
    result = base ** exponent
    print(f"{base} raised to the power of {exponent} is:", result)
    return result
power(2,3)
power(5,4)
power(10,2)
#output:
#2 raised to the power of 3 is: 8
#5 raised to the power of 4 is: 625
#10 raised to the power of 2 is: 100
##################################################################################
    