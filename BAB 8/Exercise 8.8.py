#Menulis Fungsi
def make_album(artist, title):
    album = {
        "artist": artist,
        "title": title
    }
    
    return album

#Membuat loop agar user bisa memasukkan data yang diminta
while True:
    print("Enter album information:")
    artist = input("Artist name: ")
    
    if artist == 'quit':
        break
    
    title = input("Album title: ")
    if title == 'quit':
            break

#Memanggil fungsi
    album = make_album(artist, title)
    
    print(album)
    print("================================================")