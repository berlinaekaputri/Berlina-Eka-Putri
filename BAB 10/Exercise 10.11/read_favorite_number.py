
# Exercise 10-11: Read Favorite Number

import json

# Membaca angka dari file
with open("favorite_number.json") as file_object:
    number_string = file_object.read()

# Mengubah JSON menjadi data Python
favorite_number = json.loads(number_string)

# Menampilkan angka favorit
print(f"I know your favorite number! It's {favorite_number}.")
