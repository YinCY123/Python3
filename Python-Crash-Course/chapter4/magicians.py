magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you everyone, that was a great magic show!")

for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

suqares = [value ** 2 for value in range(1, 11)]
print(squares)

for i in range(1, 21):
    print(i)

l = [x for x in range(1, 1000001)]
print(min(l))
print(max(l))
print(sum(l))

odd_number = list(range(1, 21, 2))
print(odd_number)

time3 = [x for x in range(3, 30) if x % 3 == 0]
print(time3)

x = [a ** 3 for a in range(1, 11)]
print(x)