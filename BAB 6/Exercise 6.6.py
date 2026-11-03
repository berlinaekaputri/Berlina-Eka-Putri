favorite_languages = {
'Jen': 'python',
'Sarah': 'c',
'Edward': 'rust',
'Phill': 'python',
}

nama_orang = ["Beni", "Chairul", "Jen", "Sarah", "Edward", "Lily"]

#Memeriksa orang yang sudah dan belum mengisi polling
for nama in nama_orang:
    if nama in favorite_languages:
        print(f"Terimakasih {nama} sudah merespon")
    else:
        print(f"{nama}, tolong isi polingnya ya!")