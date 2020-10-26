motorcycles = ['hinda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

# add elements to a list
motorcycles.append("ducati")
print(motorcycles)

motorcycles = []
motorcycles.append("honda")
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# insert elements to a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, "ducati")
print(motorcycles)

# removing elements from a list
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove("ducati")
print(motorcycles)

"""
The remove() method deletes only the first occurrence of the value you specify. 
If there's a possibility the value appears more than once in the list, you'll 
need to use a loop to determine if all occurrence of the value have been removed.
"""

to_invite = ["zhangsan", "wanger", "lishi"]
for name in to_invite:
    if name == "wanger":
        print("Soory about that " + name + " cannot make it.")
    else:
        print("Hello, " + name.title() + " do you have time to have dinner with me tonight?")

to_invite.append("miza")
print(to_invite)