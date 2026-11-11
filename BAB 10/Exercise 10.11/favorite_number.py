import json

# Meminta angka favorit
favorite_number = int(input("What is your favorite number? "))

# Mengubah angka menjadi format JSON
number_string = json.dumps(favorite_number)

# Menyimpan angka ke dalam file
with open("favorite_number.json", "w") as file_object:
    file_object.write(number_string)
