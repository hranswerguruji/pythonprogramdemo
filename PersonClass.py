class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute

    # Method
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
