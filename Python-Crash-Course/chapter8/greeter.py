def greet_user(username):
    '''Display a simple greeting.'''
    print("Hello, " + username.title() + "!")

greet_user('jesse')

"""
People sometimes speak of arguments and parameters interchangeably. Don't be surprised
if you see the variables in a function definition referred to as arguments or the variables 
in a function call referred to as parameters.
"""

def display_message():
    print("Hello, every one i'm now learning in chapter 8.")

display_message()


def favorite_book(title):
    print("One of my favorite book is " + title.title() + ".")

favorite_book("Alice in wonderland")