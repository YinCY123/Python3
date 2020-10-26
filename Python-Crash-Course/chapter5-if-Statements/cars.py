cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())


requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")