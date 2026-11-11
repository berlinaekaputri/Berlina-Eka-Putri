while True:
    # Meminta dua input dari pengguna
    first_number = input("Enter the first number: ")

    if first_number == "quit":
        break

    second_number = input("Enter the second number: ")

    if second_number == "quit":
        break

    try:
        # Mengubah input menjadi integer
        number_1 = int(first_number)
        number_2 = int(second_number)

        # Menjumlahkan kedua angka
        result = number_1 + number_2

    except ValueError:
        print("Sorry, please enter numbers instead of text.")

    else:
        print("The result is:", result)
