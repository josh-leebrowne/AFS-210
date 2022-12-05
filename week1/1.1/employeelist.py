class EmployeeList:
    def __init__(self):
        self.employees = []

    def addEmployees(self, employee):
        self.employees.append(employee)

    def getEmployees(self):
        print(self.employees)

