"""
Using Arbitrary keyword arguments
"""

def build_profile(first, last, **user_info):
    """build a dictionary containing everything we know about a user."""

    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einsrein',
                             location = "priceton",
                             filed = 'physics')

print(user_profile)


def Sandwiches(*items):
    print("\nThe follwoing items has been ordered: ")
    for i in items:
        print("  - " + i)

sands = Sandwiches('apple', 'pea', 'orange', 'tomato')
sands

def build_my_file(first, last, **other_info):
    file = {}
    file['first_name'] = first
    file['last_name'] = last
    for k, v in other_info.items():
        file[k] = v

    return file

my_file = build_my_file("Yin", "Chunyou", age = 30, gender = "male")
print(my_file)

def Cars(manufacturer, model, **others):
    car_file = {}
    car_file['manufacturer_name'] = manufacturer
    car_file['model_name'] = model

    for key, value in others.items():
        car_file[key] = value

    return car_file

cars = Cars("BMW", "A10", color = "grey", height = '1.6m')
print(cars)