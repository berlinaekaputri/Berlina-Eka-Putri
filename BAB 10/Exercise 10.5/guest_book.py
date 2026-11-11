# Membuat list untuk menyimpan nama
names = []

# Meminta nama pengguna secara berulang
while True:
    name = input("Please enter your name: ")

    if name == "quit":
        break

    names.append(name)

# Menuliskan semua nama ke dalam file
with open("guest_book.txt", "w") as file_object:
    for name in names:
        file_object.write(name + "\n")
