# Logical Operators

# NOT Operator
a = 10
b = 5
print(not(a>b))  # False
print(not(a<b))  # True


# AND Operator
C = 20
D = 8
E = 10
F = 30

print(C > D and E > F)  # statement1 is True and statement2 False => Final ans is False
print(C > D and E < F)  # statement1 is True and statement2 True => Final ans is True


# OR Operator
print(C > D or E > F)   # statement1 is True and statement2 False => Final ans is True
print(C > D or E < F)   # statement1 is True and statement2 True => Final ans is True
print(C < D or E > F)   # statement1 is False and statement2 False => Final ans is False