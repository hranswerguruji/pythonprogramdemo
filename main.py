import CalculatorFunction
import PersonClass
import UserInputFunction

# FunctionDemo.first_demo()

# Calculator function calling
add = CalculatorFunction.add(10, 5)
print(f"The adding of 2 number is {add}")
sub = CalculatorFunction.add(10, 5)
print(f"The subtraction of 2 number is {sub}")
mul = CalculatorFunction.add(10, 5)
print(f"The multiplication of 2 number is {mul}")
div = CalculatorFunction.add(10, 5)
print(f"The division of 2 number is {div}")

# User input function demo calling
UserInputFunction.get_user_detail()

# Class demo calling
# Creating an Object
person1 = PersonClass.Person("Santosh Kumar Singh", 22)
# Accessing attributes
print(person1.name)  # Output: Santosh Kumar Singh
print(person1.age)  # Output: 22
person1.greet()
