# Meminta pengguna memasukkan nama
name = input("Please enter your name: ")

# Membuka file dan menuliskan nama
with open("guest.txt", "w") as file_object:
    file_object.write(name)
