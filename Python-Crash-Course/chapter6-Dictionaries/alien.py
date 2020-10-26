alien_0 = {'color': "green", 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# add new key-value pairs
alien_0 = {'color': "green", 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# create an empty dictionary
alien_0 = {}
alien_0['color'] = "green"
alien_0['points'] = 5
print(alien_0)

# modifying values in a dictionary
alien_0 = {'color': 'green'}
print('The alien is ' + alien_0['color'] + ".")

alien_0['color'] = "yellow"
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': "medium"}
print("Original x_position: " + str(alien_0['x_position']))

if alien_0['speed'] == "slow":
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x_position: " + str(alien_0['x_position']))

# remove key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")

person = {'first_name': 'wang',
          'last_name': 'er',
          'age': 24,
          'city': 'hangzhou'}

for key in person:
    print(person[key])

favorite_number = {
    1: 'wanger',
    2: "zhangsan",
    3: "lisi",
    4: 'wanli'
}

for key, value in favorite_number.items():
    print(key, value)

words = {
    "list": "a list ia a collection of values.",
    "tuple": "tuple is a list but immutable.",
    "set": "set is a collection of values but no duplicates.",
    "dictionary": "dict is a collection of key-value pairs."
}
for key in words:
    print(words[key])

# one way to return items in a certain order is to sort
# the keys as thet're returned in the for loop

favorite_languages = { 'jen': 'python',
                       'sarah': 'c',
                       'edward': 'ruby',
                       'phil': 'python', }
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("\nThe following language have been mentioned: ")
for language in favorite_languages.values():
    print(language.title())

print("\nThe following people taking the poll: ")
for key in favorite_languages.keys():
    print(key)

print("\nremove repeat language: ")
for language in set(favorite_languages.values()):
    print(language.title())

rivers = {
    'nile': 'egypt',
    'huanghe': 'china',
    'changjiang': 'china',
    'missipi': 'USA',
}

for key, value in rivers.items():
    print(key.title() +
          " runs through " +
          value.title() +
          ".")

for key in rivers:
    print(key)

for country in rivers.values():
    print(country)

alien_0 = {'color': "green", 'points': 5}
alien_1 = {'color': "yellow", 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = "yellow"
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = "red"
        alien['speed'] = 'fast'
        alien['points'] = 15

print('\n')
for alien in aliens[:5]:
    print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens)))