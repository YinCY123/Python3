class Employee():
    """Employee class"""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount = 5000):
        self.annual_salary += amount
        print(self.annual_salary)

"""
my_employee = Employee("Yin", "Chunyou", 1000000)

my_employee.give_raise()
my_employee.give_raise(amount=100000)
"""