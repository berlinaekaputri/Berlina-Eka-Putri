import json

# Mengambil username yang tersimpan
def get_stored_username():
    try:
        with open("username.json") as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username


# Meminta dan menyimpan username baru
def get_new_username():
    username = input("What is your name? ")

    with open("username.json", "w") as file_object:
        json.dump(username, file_object)

    return username


# Menyambut pengguna
def greet_user():
    username = get_stored_username()

    if username:
        correct = input(f"Are you {username}? (yes/no) ")

        if correct.lower() == "yes":
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


# Menjalankan program
greet_user()
