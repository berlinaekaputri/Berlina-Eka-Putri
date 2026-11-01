list_tempat = ["Italia", "Jepang", "Spanyol", "Yunani", "Swiss"]
print(list_tempat)

#Mengurutkan List sesuai abjad
print(sorted(list_tempat))
#Menampilkan list tetap dalam original order
print(list_tempat)

#Mengurutkan list sesuai abjad terbalik
print(sorted(list_tempat, reverse=True))
#Menampilkan list tetap dalam original order
print(list_tempat)

#Membalik urutan list
list_tempat.reverse()
print(list_tempat)

#Mengubah kembali urutan list
list_tempat.reverse()
print(list_tempat)

#Mengurutkan list sesuai abjad secara permanen
list_tempat.sort()
print(list_tempat)

#Mengurutkan list sesuai abjad terbalik secara permanen
list_tempat.sort(reverse=True)
print(list_tempat)

