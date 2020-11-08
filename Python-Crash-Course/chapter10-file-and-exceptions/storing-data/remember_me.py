import json

def get_Stored_username():
    """Get stored username if available."""
    filename = "username.json"
    try:
        with open(filename, 'r') as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What's your name?")
    filename = "username.json"
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_Stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()