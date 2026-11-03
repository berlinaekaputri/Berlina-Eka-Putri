pet1 = {
    "jenis" : "Kucing",
    "owner" : "Albon"
}

pet2 = {
    "jenis" : "Anjing",
    "owner" : "Charles"
}

pet3 = {
    "jenis" : "Ikan",
    "owner" : "Lily"
}

pet4 = {
    "jenis" : "Kelinci",
    "owner" : "Oscar"
}

pets = [pet1, pet2, pet3, pet4]

#Menampilkan seluruh informasi untuk tiap tiap pet
for pet in pets:
    print("Jenis: ", pet["jenis"])
    print("Owner: ", pet["owner"])
    print("=======================================")