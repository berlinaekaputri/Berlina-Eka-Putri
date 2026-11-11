# Membuka dan membaca file
with open("learning_python.txt") as file_object:
    lines = file_object.readlines()

# Mengganti kata Python menjadi C
for line in lines:
    modified_line = line.replace("Python", "C")
    print(modified_line.strip())
