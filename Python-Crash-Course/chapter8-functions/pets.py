"""
# passing arguments

position argument
"""

def describe_pet(animal_type, pet_name):
    """
    display information about a pet.
    :param animal_type: the type of the animal.
    :param pet_name: the name you give to the animal.
    :return: a describe of the animal.
    """
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# multiple function call
describe_pet("hamster", "harry")
describe_pet("dog", 'willie')


"""
keyword arguments
"""

print("\nkeyword argument")
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

"""
default values
"""

def describe_pet(pet_name, animal_type = 'dog'):
    """Dispaly information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')
describe_pet(pet_name='willie', animal_type="hamster")


def make_shirt(size, text):
    """print a summarize of the t-shirt."""
    print("\nThe size of the T-shirt is " + str(size) +
          " and the text on it is " + text.capitalize() + ".")

make_shirt(10, "amazing")
make_shirt(size=10, text='amazing')

def describe_cities(name_of_city, country = "China"):
    print(name_of_city + " is in " + country.title() + ".")

describe_cities("hangzhou")
describe_cities("New yourk", "USA")