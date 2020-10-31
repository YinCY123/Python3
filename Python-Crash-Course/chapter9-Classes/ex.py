class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is openning.")

    def set_number_served(self, served):
        if served >= 0:
            self.number_served = served
        else:
            print("Number of served can not be negative.")

    def increment_number_served(self, num):
        if num >= 0:
            self.number_served += num
        else:
            print("Served number can not be negative.")

restaurant = Restaurant(restaurant_name="China Food", cuisine_type="Hote")
print(restaurant.number_served)

restaurant.set_number_served(20)
print(restaurant.number_served)

restaurant.increment_number_served(10)
print(restaurant.number_served)