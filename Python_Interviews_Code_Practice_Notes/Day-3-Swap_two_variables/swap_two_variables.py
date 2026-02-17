# Swap two variables:- 
# Solution-1 :- Without using third variable 
a = 10
b = 20

print(f"Before swaping two variable is : {a}, {b}")
a, b = b, a
print(f"After swaping two variables is : {a}, {b}")

#------------------------------------------------------------------------

# Solution-1 :- With using third variable 
n1 = 2
n2 = 6
print(f"Before swaping two variable is : {n1}, {n2}")

temp = n1
n1 = n2
n2 = temp
print(f"After swaping two variables is : {n1}, {n2}")


