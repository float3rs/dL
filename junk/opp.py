class Employee:

    raise_amount = 1.04
    num_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        pass

    

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 50000)

# print(emp_1)
# print(emp_2)

# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'Corey.Schafer@company.com'
# emp_1.pay = 50000

# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.user@company.com'
# emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

print('{} {}'.format(emp_1.first, emp_2.last))
print(Employee.fullname(emp_1))

print(emp_1.__dict__)
print(Employee.__dict__)

emp_1.raise_amount = 1.05
print(emp_1.__dict__)
print(emp_2.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


Employee.apply_raise(emp_1)
print(emp_1.pay)

print(Employee.num_of_emps)

emp_3 = Employee('Nikos', 'Saridakis', 100000)
print(Employee.num_of_emps)

