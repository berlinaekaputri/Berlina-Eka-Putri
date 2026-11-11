#Mendefinisikan bentuk class
class Restaurant:
#Menentukan atribut restaurant
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

# Membuat child class IceCreamStand
class IceCreamStand(Restaurant):

    # Menentukan atribut ice cream stand
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = ["Chocolate", "Vanilla", "Strawberry", "Matcha"]
        
# Menampilkan daftar rasa es krim
    def display_flavors(self):
        print("Available ice cream flavors:")

        for flavor in self.flavors:
            print(flavor)


# Membuat object IceCreamStand
ice_cream = IceCreamStand("Sweet Treats", "Ice Cream")

# Menampilkan daftar rasa es krim
ice_cream.display_flavors()
ice_cream.describe_restaurant()