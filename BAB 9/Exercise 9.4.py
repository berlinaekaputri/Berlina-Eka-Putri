# Mendefinisikan bentuk Class 
class Restaurant:
    def __init__(self, name, type):
        self.Name = name
        self.Type = type
        self.number_served = 0
        
    # Mengatur jumlah pelanggan
    def set_number_served(self, number):
        self.number_served = number

    # Menambahkan jumlah pelanggan
    def increment_number_served(self, number):
        self.number_served += number
        
    def describe_restaurant(self):
        print(f"Restaurant name: {self.Name}")
        print(f"Cuisine type: {self.Type}")

    def open_restaurant(self):
        print(f"{self.Name} is open!")
        
# Membuat object restaurant
restaurant = Restaurant("Pizza Hut", "Italian Food")

# Menampilkan jumlah pelanggan awal
print("Number served:", restaurant.number_served)

# Mengubah nilai number_served secara langsung
restaurant.number_served = 10
print("Number served:", restaurant.number_served)

# Mengatur jumlah pelanggan menggunakan method
restaurant.set_number_served(25)
print("Number served:", restaurant.number_served)

# Menambahkan jumlah pelanggan menggunakan method
restaurant.increment_number_served(15)
print("Number served:", restaurant.number_served)
