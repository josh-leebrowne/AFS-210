class Employee:
    def __init__(self, first, last, ID, hourlyPay):
        self.first = first
        self.last = last
        self.ID = ID
        self.hourlyPay = hourlyPay

    def pay(self, hours):
        if hours <= 40:
            regpay = (self.hourlyPay * hours)
            return regpay
        else:
            overtime = ((hours * 40) * 1.5)
            return overtime


first = input('Employee First Name: ')
last = input('Employee Last Name: ')
empID = int(input('Employee ID: '))
hourlyRate = float(input('Please input hourly rate: '))
hours = float(input('Employee Hours: '))

newEmployee = Employee(first, last, empID, hourlyRate)

print(f"{newEmployee.first} {newEmployee.last}'s paycheck amount is ${newEmployee.pay(hours):,.2f}")




