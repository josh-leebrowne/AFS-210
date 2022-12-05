class Employee:
    def __init__(self, first, last, ID, hours):
        self.first = first
        self.last = last
        self.ID = ID
        self.hours = hours

    def pay(self):
        if self.hours < 40 or self.hours == 40:
            regpay = (self.hours * 40)
            print(float(regpay))
        else:
            overtime = ((self.hours * 40) * 1.5)
            print(float(overtime))





