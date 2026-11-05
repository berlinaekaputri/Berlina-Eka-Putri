#Tiga program yang sesuai dengan aturan PEP
#Exercise 4.1
jenis_pizza = ["Pepperoni", "Cheese", "Neapolitan", "Margherita"]
for pizza in jenis_pizza:
    print (pizza)

for pizza in jenis_pizza:
    print(f"Aku suka makan {pizza} pizza")
    
print("Aku sangat suka makan pizza")

#Exercise 4.10
jenis_pizza = ["Pepperoni", "Cheese", "Neapolitan", "Margherita", "Marinara"]

#Menampilkan 3 item yang berada di awal
print("The first three items in the list are:")
print(jenis_pizza[:3])

#Menampilkan 3 item yang berada di tengah
print("Three items from the middle of the list are:")
print(jenis_pizza[1:4])

#Menampilkan 3 item yang berada di akhir
print("The last three items in the list are:")
print(jenis_pizza[-3:])

#Exercise 4.12
# Membuat list makanan favorit
my_foods = ["pizza", "falafel", "carrot cake"]

# Membuat list makanan favorit teman
friend_foods = ["pizza", "falafel", "ice cream"]

# Menampilkan makanan sendiri menggunakan for loop
print("My favorite foods are:")
for food in my_foods:
    print(food)

# Menampilkan makanan teman menggunakan for loop
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)
