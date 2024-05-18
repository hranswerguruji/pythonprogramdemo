from Employee import Employee


class EmpDetail(Employee):
    def __init__(self):
        super().__init__()
        self.department_name = None

    def department(self):
        print(f"The department is {self.department_name}")
