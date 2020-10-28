# create the dog class
class Dog():
    """a simple attempt to model a dog."""

    def __init__(self, name, age):
        """initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

"""
A function that's part of a class is a method, everything you learned 
about functions applies to methods as well, the only practical difference 
for now is the way we'll call methods.

Any variable prefixed with self is available to every method in the class, and
we'll also be able to access these variables through any instance created from 
the class.
"""

# making an instance from a class

my_dog = Dog(name = "willie", age = 6)
print("my dog's name is " + my_dog.name.title() + ".")
print("my dog is " + str(my_dog.age) + " years old.")

my_dog = Dog(name = "willie", age = 6)
your_dog = Dog(name = "lucy", age = 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " year old.")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is openning.")

restaurant = Restaurant(restaurant_name="china food", cuisine_type="north")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("\nThe first name of you is: " + self.first_name.title())
        print("The last name of you is: " + self.last_name.title())

    def greet_user(self):
        print("Hello, " + self.first_name + " " + self.last_name.title() + "!")

user_profile = User(first_name="Yin", last_name="Chunyou")
user_profile.describe_user()
user_profile.greet_user()