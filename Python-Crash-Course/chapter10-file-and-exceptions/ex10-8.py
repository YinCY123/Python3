files = ['cats.txt', 'dogs.txt', "abs.txt"]

for file in files:
    try:
        with open(file) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        #print("The file " + file + " is not found.")
        pass # fail silently
    else:
        print(contents)