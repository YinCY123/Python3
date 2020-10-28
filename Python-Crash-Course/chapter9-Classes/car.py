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

my_new_car = Car(make="audi", model="a4", year=2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# modifying an attribute's value directly
my_new_car.odometer_reading = 10
my_new_car.read_odometer()

my_new_car.update_odometer(mileage=20)
my_new_car.read_odometer()

my_new_car.update_odometer(mileage=-20)
my_new_car.read_odometer()

"""
Every attribute in a class needs an initial value, even if that value is 0 or an empty string.
"""