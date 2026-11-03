favorite_places = {
    "Max" : ["Monaco", "Belanda", "Italia"],
    "Gasly" : ["Prancis", "Spanyol", "Swiss"],
    "Yuki" : ["Jepang", "Korea", "China"],
}

#Menampilkan nama setiap orang beserta tempat favorit
for name, places in favorite_places.items():
    print(name + "'s favorite places are:")
    
    for place in places:
        print("- " + place)
        
    print("=======================================")

