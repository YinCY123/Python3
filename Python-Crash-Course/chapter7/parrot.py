prompt = input("Tell me something, and I will repeat it back to you: ")
prompt += "\nEnter 'quit' or 'q' to end the program."
message = ''
while message not in ["quit", 'q']:
    message = input(prompt)
    print(message)

# using a flag
prompt = input("tell me something, and I will repeat it back to you: ")
prompt += "\nEnter 'quit' or 'q' to end the program."
active = True
while active:
    message = input(prompt)
    if message in ['quit', 'q']:
        #active = False
        break
    else:
        print(message)