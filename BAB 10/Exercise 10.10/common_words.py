with open("dorian gray.txt", encoding="utf-8") as file_object:
    contents = file_object.read()

# Menghitung kemunculan kata 'the'
the_count = contents.lower().count("the")
print("The word 'the' appears", the_count, "times in Dorian Gray.")

# Menghitung kemunculan kata 'the ' yang diikuti spasi
the_space_count = contents.lower().count("the ")
print("The word 'the ' appears", the_space_count, "times in Dorian Gray.")