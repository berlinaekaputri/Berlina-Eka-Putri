# Membuka dan membaca seluruh isi file
with open("learning_python.txt") as file_object:
    contents = file_object.read()

# Menampilkan setiap baris tanpa variabel sementara
for line in contents.splitlines():
    print(line)
