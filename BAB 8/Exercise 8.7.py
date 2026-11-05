#Menulis fungsi
def make_album(artist, title, songs = None):
    album = {
        "artist": artist,
        "title": title
    }
# Memeriksa nilai dari songs apakah none atau bukan     
    if songs is not None:
        album['songs'] = songs

#Mengembalikan hasil dari fungsi
    return album

#Memanggil fungsi
album1 = make_album("Taylor Swift", "1989")
album2 = make_album("Adele", "25")
album3 = make_album("Coldplay", "Parachutes")
album4 = make_album("Taylor Swift", "Midnights", songs=13)

print(album1)
print(album2)
print(album3)
print(album4)