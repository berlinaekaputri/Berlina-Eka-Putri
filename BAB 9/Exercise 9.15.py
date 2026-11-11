import random

# Daftar angka dan huruf untuk lottery
lottery_numbers = [
    1, 3, 5, 7, 9,
    2, 4, 6, 8, 10,
    "A", "B", "C", "D", "E"
]

# Tiket yang kita miliki
my_ticket = [7, "B", 1, "C"]

# Menghitung jumlah percobaan
attempts = 0
while True:
    winning_ticket = random.sample(lottery_numbers, 4)
    attempts += 1
    
    if winning_ticket == my_ticket:
        break

# Menampilkan hasil
print("My ticket:", my_ticket)
print("Winning ticket:", winning_ticket)
print(f"It took {attempts} attempts to win!")