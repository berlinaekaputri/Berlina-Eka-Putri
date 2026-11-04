dream_vacations = {}

polling_active = True

#Membuat perulangan untuk menginput data user
while polling_active:
    name = input("What is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    dream_vacations[name] = place

    repeat = input("Would you like to let another person respond? (yes/no) ")

    if repeat == 'no':
        polling_active = False

#Menampilkan hasil data ketika users sudah memasukkan input
print("\n--- Dream Vacation Poll Results ---")

for name, place in dream_vacations.items():
    print(f"{name} would like to visit {place}.")