from employeelist import EmployeeList
from payroll import Employee

my_List = EmployeeList()


first = input('Employee First Name: ')
last = input('Employee Last Name: ')
ID = input('Employee ID: ')
hours = input('Employee Hours: ')

my_Employees = Employee(first, last, ID, hours)
my_List.addEmployees(my_Employees)


