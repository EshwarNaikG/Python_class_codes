# a = "hi"
# b = "hi"
# print(a == b) # True
# print(a is b) # May be True or False
# print(id(a))
# print(id(b))

# #-----------------------------------------------

# s = "python"
# print(s.find('z')) # -1
# # print(s.index('z')) ❌ Error

a = [1, 2]
print(a)
a.append(3)        # Add at end
print(a)

a.insert(1, 10)    # Add at index
print(a)

a.extend([4, 5])   # Add multiple values
print(a)

#---------------------------------------------
a = [10, 20, 30, 20]
print(a)

a.remove(20)   # Removes first occurrence
print(a)

a.pop()        # Removes last element
print(a)

a.pop(1)       # Removes index element
print(a)

a.clear()      # Removes all elements
print(a)

#---------------------------------------------
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(fruits[i])

#---------------------------------------------
a = [10, 20, 30]

for i in a:
    print(i)
#---------------------------------------------