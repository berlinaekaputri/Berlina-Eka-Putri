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