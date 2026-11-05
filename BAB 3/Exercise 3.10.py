# Membuat list berisi nama sirkuit F1
circuits = ["Monza", "Silverstone", "Monaco", "Suzuka", "Spa"]

# Menampilkan list awal
print("Original list:")
print(circuits)

# Mengakses elemen berdasarkan indeks
print("\nAccessing an element:")
print(circuits[0])

# Mengubah elemen dalam list
circuits[1] = "Bahrain"
print("\nAfter changing an element:")
print(circuits)

# Menambahkan elemen di akhir list
circuits.append("Zandvoort")
print("\nAfter append():")
print(circuits)

# Menambahkan elemen pada posisi tertentu
circuits.insert(2, "Singapore")
print("\nAfter insert():")
print(circuits)

# Menghapus elemen berdasarkan nilai
circuits.remove("Monaco")
print("\nAfter remove():")
print(circuits)

# Menghapus elemen berdasarkan indeks
del circuits[0]
print("\nAfter del:")
print(circuits)

# Menghapus elemen terakhir dan menyimpannya
popped_circuit = circuits.pop()
print("\nAfter pop():")
print(circuits)
print("Removed circuit:", popped_circuit)

# Mengurutkan list secara alfabetis
circuits.sort()
print("\nAfter sort():")
print(circuits)

# Mengurutkan list secara alfabetis terbalik
circuits.sort(reverse=True)
print("\nAfter sort(reverse=True):")
print(circuits)

# Menampilkan list dengan urutan terbalik sementara
print("\nUsing sorted() in reverse order:")
print(sorted(circuits, reverse=True))

# Menghitung jumlah elemen dalam list
print("\nNumber of circuits:")
print(len(circuits))

# Membalik urutan list secara permanen
circuits.reverse()
print("\nAfter reverse():")
print(circuits)