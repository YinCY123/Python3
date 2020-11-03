try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divid by zero!")

print("Give me two numbers, and i'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input('Second number: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
        # any code that depends on the try block executing successfully goes in the else block.
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)