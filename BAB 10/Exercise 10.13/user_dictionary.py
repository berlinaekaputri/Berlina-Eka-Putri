import json

# Meminta informasi pengguna
username = input("What is your name? ")
favorite_team = input("What is your favorite F1 team? ")
hobby = input("What is your hobby? ")

# Menyimpan informasi dalam dictionary
user_info = {
    "username": username,
    "favorite_team": favorite_team,
    "hobby": hobby
}

# Mengubah dictionary menjadi JSON
user_string = json.dumps(user_info)

# Menyimpan data ke file
with open("user_info.json", "w") as file_object:
    file_object.write(user_string)

# Membaca data dari file
with open("user_info.json") as file_object:
    user_string = file_object.read()

# Mengubah JSON menjadi dictionary
user_info = json.loads(user_string)

# Menampilkan ringkasan informasi
print("\nHere's what I know about you:")
print("Name:", user_info["username"])
print("Favorite F1 Team:", user_info["favorite_team"])
print("Hobby:", user_info["hobby"])
