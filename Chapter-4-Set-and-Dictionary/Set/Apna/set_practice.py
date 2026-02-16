# 2. You are given a list of subjects for students. Assume 1 class room is required for 1 subject.
# How many class romms are need by all students.

class_rooms = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}

print(class_rooms)
print(len(class_rooms))

#----------------------------------------------------------------------------------------------


# 4. Figure out a way to store 9 & 9.0 as separate values in the set.
# ( you can take help of built-in data types)

values = {9, 9.0}
print(values)

values= {9, "9.0"} # Both values save using 1 is integer(number) and another is string.
print(values)