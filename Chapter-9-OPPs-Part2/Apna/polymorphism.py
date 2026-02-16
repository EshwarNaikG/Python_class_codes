# 🔄 7. Polymorphism :-
"""Same method name, different behavior."""

# 🔹 Method Overriding
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

# 🔹 Operator Overloading
print(5 + 3)        # 8
print("Hi " + "All")  # Hi All
