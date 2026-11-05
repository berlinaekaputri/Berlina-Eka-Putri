# Membuat dictionary berisi angka favorit dan tim pembalap F1
favorite_numbers = {
    "Martin": {
        "numbers": [7, 9, 13],
        "team": "Aprilia Racing"
    },

    "Charles": {
        "numbers": [16, 1, 33],
        "team": "Ferrari"
    },

    "Carlos": {
        "numbers": [55, 23, 70],
        "team": "Williams"
    },

    "Kimi": {
        "numbers": [27, 4, 81],
        "team": "Mercedes"
    },

    "Rafa": {
        "numbers": [53, 6, 71],
        "team": "Racing Bulls"
    }
}

# Menampilkan informasi setiap pembalap
for name, information in favorite_numbers.items():
    print("\nDriver:", name)

    # Menampilkan tim pembalap
    print("Team:", information["team"])

    # Menampilkan angka favorit
    print("Favorite numbers:")

    for number in information["numbers"]:
        print(number)