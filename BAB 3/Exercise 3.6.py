# Membuat list berisi nama
guests = ["Max Verstappen", "Kimi Raikkonen", "Lewis Hamilton"]

# Memberitahu bahwa meja makan yang lebih besar telah ditemukan
print("Good news! I found a bigger dinner table.")

# Menambahkan nama baru di awal list
guests.insert(0, "Lando Norris")

# Menambahkan nama baru di tengah list
guests.insert(2, "Oscar Piastri")

# Menambahkan nama baru di akhir list
guests.append("George Russell")

# Menampilkan undangan untuk semua pembalap
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")