# Membuat list berisi enam nama
guests = [
    "Lando Norris",
    "Max Verstappen",
    "Oscar Piastri",
    "Kimi Raikkonen",
    "Lewis Hamilton",
    "George Russell"
]

# Memberitahu bahwa hanya dua nama yang bisa diundang
print("Sorry, I can only invite two people to dinner.")

# Menghapus nama tamu sampai tersisa dua orang
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")

# Memberitahu dua nama tamu yang masih diundang
for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner.")

# Menghapus dua nama yang tersisa
del guests[0]
del guests[0]

# Menampilkan list untuk memastikan sudah kosong
print("\nFinal guest list:")
print(guests)