# EXERCISE 8-2: FAVORITE BOOK

# Fungsi untuk menampilkan buku favorit
def favorite_book(title):
    """Menampilkan judul buku favorit."""

    # Menampilkan pesan tentang buku favorit
    print("One of my favorite books is " + title)


# Memanggil fungsi
favorite_book("Dead Poets Society")

print("==================================================")
# EXERCISE 8-6: CITY NAMES

# Menulis fungsi untuk menggabungkan nama kota dan negara
def city_country(city, country):
    """Mengembalikan nama kota dan negara."""

    # Menggabungkan kota dan negara
    result = city + ", " + country

    # Mengembalikan hasil penggabungan
    return result


# Memanggil fungsi dan menampilkan hasilnya
print(city_country("Roma", "Italia"))
print(city_country("Jakarta", "Indonesia"))
print(city_country("Tokyo", "Jepang"))


print("==================================================")
# EXERCISE 8-7: ALBUM

# Fungsi untuk menyimpan informasi album
def make_album(artist, title, songs=None):
    """Membuat dictionary yang berisi informasi album."""

    # Membuat dictionary album
    album = {
        'artist': artist,
        'title': title
    }

    # Memeriksa apakah jumlah lagu diberikan
    if songs is not None:

        # Menambahkan jumlah lagu ke dictionary
        album['songs'] = songs

    # Mengembalikan dictionary album
    return album


# Membuat tiga album dengan informasi berbeda
album1 = make_album("Taylor Swift", "1989")
album2 = make_album("Adele", "25")
album3 = make_album("Coldplay", "Parachutes", songs=12)

# Menampilkan informasi album
print(album1)
print(album2)
print(album3)