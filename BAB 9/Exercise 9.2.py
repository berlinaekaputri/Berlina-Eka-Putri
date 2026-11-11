# Mendefinisikan bentuk Class 
class Restaurant:
    def __init__(self, name, type):
        self.Name = name
        self.Type = type
        
#menampilkan nama dan jenis makanan restoran
    def describe_restaurant(self):
        print("Restaurant name: " + self.Name)
        print("Cuisine type: " + self.Type)
        
# Membuat object
restaurant1 = Restaurant("Pizza Hut", "Italian Food")
restaurant2 = Restaurant("KFC", "Fast Food")
restaurant3 = Restaurant("Sushi Hiro", "Japanese Food")

# Memanggil method
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()