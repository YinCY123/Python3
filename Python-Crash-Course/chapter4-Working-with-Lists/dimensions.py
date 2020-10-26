dimensions = (200, 50)
print(dimensions)
print(dimensions[1])

# dimensions[1] = 100

for dimension in dimensions:
    print(dimension)

dimensions = (200, 50)
print("original dimensions")
for dimension in dimensions:
    print(dimension)

dimensions = (100, 50)
print("\nmodified dimensions")
for dimension in dimensions:
    print(dimension)