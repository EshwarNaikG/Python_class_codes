# WAP to ask the user to enter names of their 3 favorite movies and store them in a list.
movies = []    # Create empty list
movies1 = input("enter first movie name : ")  # user input
movies2 = input("enter second movie name : ") # user input
movies3 = input("enter third movie name : ")  # user input

movies.append(movies1) # add fist movie in list
movies.append(movies2) # add second movie in list
movies.append(movies3) # add third movie in list

print(movies)

#--------------------------------------------------------------------------
# WAP to ask the user to enter names of their 3 favorite cities and store them in a list.

cities = []  # Empty list
cities.append(input("Enter your first city : "))
cities.append(input("Enter your second city : "))
cities.append(input("Enter your third city : "))

print(cities)

#--------------------------------------------------------------------------------

# WAP to check if a list contains palindrome of elements (Hint: use copy() method )
# Example-1 : Palindrome
list1 = [1,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("NOT a Palindrome")
#---------------------------------------------------------
# Example-2   : NOT Palindrome
list2 = [1,2,3]

copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("Palindrome")
else:
    print("NOT a Palindrome")