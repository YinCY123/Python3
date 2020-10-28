import module

module.make_pizza(16, "pepperoni")
module.make_pizza(12, "mushroom", "green peppers", "extra cheese")


# importing specific functions
from module import make_pizza
make_pizza(16, "pepperoni")
make_pizza(12, "mushroom", "green peppers", "extra cheese")


# using as to give a function an alias
from module import make_pizza as mp
mp(16, "pepperoni")
mp(12, "mushroom", "green peppers", "extra cheese")

# using as to give a module an alias
import module as p
p.make_pizza(16, "pepperoni")
p.make_pizza(12, "mushroom", "green peppers", "extra cheese")

# importing all functions in a module
from module import *
make_pizza(16, "peppers")
make_pizza(12, "mushroom", "green peppers", "extra cheese")