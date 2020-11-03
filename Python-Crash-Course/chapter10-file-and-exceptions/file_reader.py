with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

"""
The keyword with closes the file once access to it is no longer needed.
"""

"""
readng line by line 
"""

filename = "pi_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()
    # pi_string += line.strip()
    # pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))

'''
making a list of lines from a file

When you use with, the file object returned by open() is only available inside the with
block that contains it.

If you want to retain access to a file's contents outside the with block, you can store
the file's lines in a list inside the block and then work with that list.
'''

filename = "pi_million_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")


filepath = "learning_python.txt"
with open(filepath) as file:
    lines = file.readlines()

for line in lines:
    print(line * 3)

for line in lines:
    print(line.replace('Python', "C"))