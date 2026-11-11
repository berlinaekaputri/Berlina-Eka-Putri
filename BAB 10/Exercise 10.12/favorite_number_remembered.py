import json
# Memeriksa apakah file angka favorit tersedia
try:
    with open("favorite_number.json") as file_object:
        number_string = file_object.read()

# Jika file belum tersedia, meminta angka favorit
except FileNotFoundError:
    favorite_number = int(input("What is your favorite number? "))
    number_string = json.dumps(favorite_number)

    with open("favorite_number.json", "w") as file_object:
        file_object.write(number_string)

    print("Your favorite number has been saved!")

# Jika file sudah tersedia, menampilkan angka favorit
else:
    favorite_number = json.loads(number_string)
    print(f"I know your favorite number! It's {favorite_number}.")
