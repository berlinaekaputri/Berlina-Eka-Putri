# Membuat list berisi nama tamu
guests = ["Max Verstappen", "Kimi Raikkonen", "Lewis Hamilton"]

# Menampilkan undangan awal
for guest in guests:
    print(f"Dear {guest}, I would like to invite you to dinner.")

# Memberitahu tamu yang tidak bisa hadir
print(f"\nUnfortunately, {guests[1]} can't make it to dinner.")

# Mengganti nama tamu yang tidak bisa hadir
guests[1] = "Nikola Tesla"

# Menampilkan undangan baru
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")