class Employee:
    def __init__(self):
        self.name = None
        self.emp_id = None
        self.salary = None

    def employee_detail(self):
        print(f"Employee Id: {self.emp_id} , name: {self.name} and salary is {self.salary}")

    def department(self):
        raise NotImplementedError("Subclass must implement abstract method")
