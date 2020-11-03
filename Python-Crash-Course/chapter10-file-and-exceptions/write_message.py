filename = "programming.txt"

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

"""
You can open a file in read mode ('r'), write mode ('w'),
append mode ('a'), or a mode that allows you to read and write
to the file ('r+'). 

If you omit the mode argument, Python opens the file in read-only 
mode by default. 

The open() function automatically creates the file you're writing 
to if it doesn't already exist. 

However, be careful opening a file in write mode ('w') because if
the file does exist, Python will erase the file before returning 
the file object.

Python can only write strings to a text file, if you want to store 
numerical data in a text file, you will have to convert the data to 
string format first using the str() function.
"""


filepath = "guest.txt"
flag = True
while flag:
    name = input("Please enter your name: ")
    if name:
        print("Welcome " + name.title() + "!")
        with open(filepath, 'a') as file:
            file.write(name + "\n")
    else:
        flag = False