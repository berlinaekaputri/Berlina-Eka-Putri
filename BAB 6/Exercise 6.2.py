favorite_numbers = {
    "Martin" : 7,
    "Charles" : 16,
    "Carlos" : 55,
    "Kimi" : 27,
    "Rafa" : 53
}

print("Angka favorite sahabatku:")

#Memanggil key dan value dari dictionary
for name, number in favorite_numbers.items():
    print(f"{name}: {number}")