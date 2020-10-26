# 7 -8 Deli
sandwich_orders = ["apple", "banana", "pea", "orange"]
finished_sandwiches = []

while sandwich_orders:
    print("I made your " + sandwich_orders.pop().title() + " sandwiches.")

print("\nAll sandwiches have been made.")

sandwich_orders = ["apple", "pastrami", "banana", "pastrami", "pea", "pastrami", "orange"]

print("\nThe deli has run out of pastrami.")
for i in sandwich_orders:
    if "pastrami" in sandwich_orders:
        sandwich_orders.remove("pastrami")

print(sandwich_orders)