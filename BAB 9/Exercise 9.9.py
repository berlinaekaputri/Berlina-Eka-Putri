class Car:
    # Menentukan atribut mobil
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    # Membuat class Battery
class Battery:
    # Menentukan kapasitas baterai
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
    
    # Menampilkan jarak tempuh mobil
    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print("This car can go about " + str(range) + " miles on a full charge.")
    
    # Meningkatkan kapasitas baterai
    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
            
# Membuat child class ElectricCar
class ElectricCar(Car):
        # Menentukan atribut mobil listrik
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

# Membuat object ElectricCar
my_car = ElectricCar("Tesla", "Model S", 2026)

# Menampilkan jarak tempuh sebelum upgrade
my_car.battery.get_range()

# Meningkatkan kapasitas baterai
my_car.battery.upgrade_battery()

# Menampilkan jarak tempuh setelah upgrade
my_car.battery.get_range()

