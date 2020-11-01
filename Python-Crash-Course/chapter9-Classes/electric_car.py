class Car():
    """A simple attempt to represnet a car."""
    def __init__(self, make, model, year):
        """initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """return a neatly formatted descriptive name."""
        long_name = str(self.year) + " " + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """print a statement showing the car's mileage"""
        print("\nThis car has " + str(self.odometer_reading) + " miles on it.")

    """modify an attibute through a method"""
    def update_odometer(self, mileage):
        if mileage < 0:
            print("You can't roll back the odometer!")
        else:
            self.odometer_reading += mileage

"""
when you create a child class, the parent class must be part of the current file
and must appear before the child class in the file.
"""

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size = 70):
        """initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print("\n" + message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    """represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery() # instance as attributes

    def describe_battery(self):
        """print a statement describing the battery size."""
        print("\nThis car has a " + str(self.battery) + "-kWh battery.")

    def fill_gas_tank(self):
        """electric car don't have gas tanks."""
        print("This car don't need a gas tank!")

"""
The super() function is a special function that helps Python make connections between 
the parent and child class.
"""

my_tesla = ElectricCar(make='tesla', model='model S', year=2016)
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()

my_tesla.battery.battery_size = 85
my_tesla.battery.get_range()

my_tesla.battery.battery_size = 70
my_tesla.battery.get_range()

my_car = ElectricCar("tesla", "model 3", year=2018)
my_car.battery.get_range()
my_car.battery.upgrade_battery()
my_car.battery.get_range()
"""
Overriding methods from the parent class

You can override any method from the parent class that doesn't fit what you're 
trying to model with the child class. To do this, you define a method in the 
child class with the same names as the method you want to override in the parent
class.
"""

"""
Instance as attributes

When you modeling something from the real world in code, you may find that you're
adding more and more detail to a class. You'll find that you have a growing list of 
attributes and methods and that your files are becoming lengthy. In these situations, 
you might recognize that part of one class can be written as a separate class. You can 
break your large class into smaller classes that work together.
"""