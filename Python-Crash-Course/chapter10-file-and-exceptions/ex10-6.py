print("Enter two numbers and we will add them.")
print("\nEnter 'q' to quit.")

flag = True
while flag:
    first_num = input("Enter the first number:")

    if first_num == 'q':
        break

    try:
        first_num = int(first_num)
    except ValueError:
        print("It seems that your first number is not numeric.")

    second_num = input("Enter the second number:")
    if second_num == "q":
        break

    try:
        second_num = int(second_num)
    except ValueError:
        print("It seems that your second number is not numeric.")

    if first_num or first_num:
        flag = True

    try:
        add = first_num + second_num
    except TypeError:
        print("One of the value is not numberic.")
    else:
        print("The sum of the two numbers is: " + str(add) + ".")