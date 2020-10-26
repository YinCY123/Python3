"""
a function can return any kind of value you need it to, include more
complicated data structures like lists and dictionaries.
"""

def build_person(first_name, last_name):
    """return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)