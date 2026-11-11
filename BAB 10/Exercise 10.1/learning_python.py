# Membuka dan membaca seluruh isi file
with open("learning_python.txt") as file_object:
    contents = file_object.read()

print("Reading the entire file:")
print(contents)


# Membuka file dan menyimpan setiap baris ke dalam list
with open("learning_python.txt") as file_object:
    lines = file_object.readlines()

print("Reading the file using a list and loop:")
for line in lines:
    print(line.strip())
