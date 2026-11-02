favorite_pizzas = ["Pepperoni", "Cheese", "Neapolitan", "Margherita", "Marinara"]
friend_pizzas = favorite_pizzas[:]

#Menambahkan jenis pizza baru ke dalam original list
favorite_pizzas.append("Mushroom pizza")
friend_pizzas.append("Calzone pizza")

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print(pizza)
    
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)