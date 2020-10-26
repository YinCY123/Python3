# sorting a list permanently with sort() method
cars = ["bmw", 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# sorting a list temporarily with sorted() function
cars = ["bmw", 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))
print(cars)

cars = ["bmw", 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

cars = ["bmw", 'audi', 'toyota', 'subaru']
print(len(cars))

locations = ["huangshan", "gulin", "yunnan", "beijing", "taisan"]
print(locations)
print(sorted(locations))
print(locations)

locations.reverse()
print(locations)

locations.reverse()
print(locations)

locations.sort()
print(locations)

locations.sort(reverse=True)
print(locations)