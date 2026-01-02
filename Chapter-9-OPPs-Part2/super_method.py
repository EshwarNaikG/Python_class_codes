# Super Method :
""" Super() method is used to access methods of the parent class """

# Example:

class Car:           # Parent class or Base class
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started....")

    @staticmethod
    def stop():
        print("Car stopped...")

class ToyotaCar(Car):          # Child class derived  Parent class
    def __init__(self, name, type):
        super().__init__(type)      #super() method is used access methods of the parent class
        super().start()             # super method access parent class methods
        super().stop()               # super method access parent class methods
        self.name = name
      
car1 = ToyotaCar("Fortune", "Electric")
print(car1.type)
print(car1.name)
