"""
passing an arbitrary number of arguments
"""

def make_pizza(*toppings):
    """print the list of toppings have been requested."""
    print("\nMaking the pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')

"""
The asterisk in the parameter name *toppings tells python to make an 
empty tuple called toppings and pack whatever values it receives into this tuple.
"""



"""
mixing positional and arbitrary arguments
"""
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'peperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')