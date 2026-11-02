basic_food = ("Steak", "Soup", "Burger", "Sushi", "Pizza")
print("The restaurant offers:")
for food in basic_food:
    print(food)

#Mengubah isi Tuple
basic_food[1] = "Noodle"

#Tuple yang baru
basic_food = ("Steak", "Soup", "Meatball", "Sushi", "Noodle")
for food in basic_food:
    print(food)