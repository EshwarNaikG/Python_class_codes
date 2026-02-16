# Private Attributes & Methods :
# Conceptual Implementations in Python
""" Private attributes & methods are meant to be used only within the class 
and are not accessible from  outside the class """


# Note :- Private attributes & methods are created using __(underscore) symboles.

# Private Methods:
#Example-1

# class Person:
#     __name = "anonymous"    #private attributes

#     def __hello():     # Private methods
#         print("hello Person!")
# p1 = Person()

#Private attributes & Private methods calling from outside the class
# print(p1.__name)

# print(p1.__hello())

#------------------------------------------------------------------------------------

#Example-2
class Person:
    __name = "anonymous"    # Private attributes

    def __hello(self):   # Private method
        print("Hello Person!")

    def welcome(self):   # Public method
        self.__hello()   #class method calls to private method  only within the class.
        print(self.__name) # class method calls to private attribute only within the class.

p1 = Person()
print(p1.welcome())  # Object calls public methods from outside the class
# Note :- Private methods access only inside the class function.
# Private methos & Attributes are not accessible from outside the class
#------------------------------------------------------------------------------------

