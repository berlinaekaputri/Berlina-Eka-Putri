# Mendefinisikan bentuk Class 
class Restaurant:
    def __init__(self, name, type):
        self.Name = name
        self.Type = type
        
#menampilkan nama dan jenis makanan restoran
    def describe_restaurant(self):
        print("Restaurant name: " + self.Name)
        print("Cuisine type: " + self.Type)

#Menampilkan pesan bahwa restaurant sudah buka
    def open_restaurant(self):
        print(self.Name + " is open!")
        
# Membuat object
restaurant = Restaurant("Pizza Hut", "Italian Food")

# Menampilkan atribut secara individu
print(restaurant.Name)
print(restaurant.Type)

# Memanggil method
restaurant.describe_restaurant()
restaurant.open_restaurant()