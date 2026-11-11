import random

# Membuat list berisi 10 angka dan 5 huruf
lottery_numbers = [
    1, 3, 5, 7, 9,
    2, 4, 6, 8, 10,
    "A", "B", "C", "D", "E"
]

# Memilih 4 angka atau huruf secara acak
winning_ticket = random.sample(lottery_numbers, 4)

# Menampilkan karakter yang terpilih
print("Winning ticket:")
print(winning_ticket)

# Menampilkan pesan pemenang
print("\nAny ticket matching these 4 numbers or letters wins a prize!")
