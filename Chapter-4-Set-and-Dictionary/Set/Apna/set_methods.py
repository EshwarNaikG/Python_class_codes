# Set Methods :

s = set()  # empty set

# add method: Adds an elements
s.add(1)
s.add(2)
s.add(3)
s.add("Eshwar")
s.add("Adithya")
s.add("bangalore")
s.add(10.7)

print(s)
print(len(s))

# remove method: Removes the element on set
s.remove(3)
s.remove(10.7)
print(s)


# Pop Method: Removes a random value
s.pop()
print(s)
print(s.pop())
print(s.pop())

# Clear Method: Empties the set (removes all elements from set)
s.clear()
print(s)



