
# Exercise 10-6: Addition

try:
    # Meminta dua angka dari pengguna
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the second number: "))

    # Menjumlahkan kedua angka
    result = number_1 + number_2

    # Menampilkan hasil
    print("The result is:", result)

except ValueError:
    print("Sorry, please enter numbers instead of text.")
