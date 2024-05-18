import CalculatorFunction
import PersonClass
import UserInputFunction
from Employee import Employee
from EmployeeDetail import EmpDetail

"""
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
"""

"""
from prettytable import PrettyTable


table = PrettyTable()
table.field_names = ["Name", "Email", "Age"]
table.add_row(["Santosh Kumar Singh", "santosh3033@gmail.com", 12])
table.add_row(["Om Sharma", "om@test.com", 20])
table.align = "l"
print(table)

"""
"""
emp = Employee()
emp.emp_id = 1001
emp.name = "Santosh"
emp.salary = 12300
emp.employee_detail()
"""
empDetail = EmpDetail()
empDetail.emp_id = 1002
empDetail.name = "Pooja Gupta"
empDetail.salary = 13400
empDetail.department_name = "IT"
empDetail.employee_detail()
empDetail.department()
