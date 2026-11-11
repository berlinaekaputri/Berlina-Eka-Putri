# Membaca file cats.txt
try:
    with open("cats.txt") as file_object:
        cats = file_object.read()
    print("Cat names:")
    print(cats)

except FileNotFoundError:
    print("Sorry, the file cats.txt was not found.")

# Membaca file dogs.txt
try:
    with open("dogs.txt") as file_object:
        dogs = file_object.read()
    print("Dog names:")
    print(dogs)

except FileNotFoundError:
    print("Sorry, the file dogs.txt was not found.")
