# what is while loop in python ?
''' In python, a while loop is a control flow statement  that repeatedly executes a block of code
as long as a given condition is true.'''

# Syntax of while loop
'''
while condition:
    # code block to be executed
'''
# # Example of while loop
# count= 0
# while count <= 5:
#     print('count is : ',count)
#     count += 1  # increment the count by 1

# # example 2 : print number from 1 to 10 (Ascening order)
# i = 1
# while i <= 10:
#     print(i)
#     i +=1

# # Example 3 : print number from 10 to 1 (Descending order)
# i = 10
# while i >=1 :
#     print(i)
#     i -= 1


# PRACTICE 

# # 1. print number from 1 to 100 (Ascening order)
# i = 1
# while i <= 100:
#     print(i)
#     i +=1

# # 2. print number from 100 to 1 (Descending order)
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# # 3. Print the multiplication table of number n using while loop
# n = int(input('Enter a number : '))
# i = 1
# while i <= 10 :
#     print(n*i)
#     i += 1

# # 4. Print the elements of the following list using a while loop
# nums = [1,4,9,16,25,36,49,64,81,100]   # List written in square brackets
# # print(len(nums))  
# index = 0
# while index < len(nums):
#     print(nums[index])
#     index += 1

# OR example-2
 
# heroes = ['Eshwar', 'Adithya', 'Superman', 'Ironman']
# i=0
# while i < len(heroes) :
#     print(heroes[i])
#     i += 1


# search for a number x in this tupple using while loop

nums = (1,4,9,16,25,36,49,64,81,100)    # Tupple  written in side a paranthesis
x = int(input('Enter a number X : '))
i = 0
while i < len(nums) :
    if(nums[i] == x) :
        print('Found at index' , i)        
    i += 1
