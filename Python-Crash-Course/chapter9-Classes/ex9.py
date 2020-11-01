class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is openning.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['apple', 'orange', 'tomato']

    def display_flavors(self):
        print("Ice creame have following flavors: ")
        for flavor in self.flavors:
            print(" - " + flavor)

ice = IceCreamStand(restaurant_name="icecreame", cuisine_type='cool')
ice.display_flavors()

# ---------------------------------------------------------------------------

class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("\nThe first name of you is: " + self.first_name.title())
        print("The last name of you is: " + self.last_name.title())

    def greet_user(self):
        print("Hello, " + self.first_name + " " + self.last_name.title() + "!")


class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can add user']

    def show_privileges(self):
        print("\nAdmin has the following privileges: ")
        for privilege in self.privileges:
            print(" - " + privilege)


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


adm = Admin("Yin", 'Chunyou')
adm.privileges.show_privileges()

# -----------------------------------------------------------------------------
"""
import a single class
"""

from car import Car
my_new_car = Car("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())