favorite_numbers = {
    "Martin" : [7, 9, 13],
    "Charles" : [16, 1, 33],
    "Carlos" : [55, 23, 70],
    "Kimi" : [27, 4, 81],
    "Rafa" : [53, 6, 71]
}

#Menampilkan nama orang dan angka favoritnya
for name, numbers in favorite_numbers.items():
    print(name + "'s favorite numbers are:")

    for number in numbers:
        print(number)

    print("=====================================")