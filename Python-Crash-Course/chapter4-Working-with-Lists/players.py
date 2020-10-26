players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])
print(players[::-1])
print(players[::2])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player)

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # copy an list
print("My favorite foods are: ")
print(my_foods)

print("\nMy friends food's are: ")
print(friend_foods)

my_foods.append("cannoli")
print(my_foods)
print(friend_foods)