# Mendefinisikan bentuk Class 
class User:  
# Menentukan atribut pengguna
    def __init__(self, first_name, last_name, age, city, username):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.username = username
        
    # Menampilkan informasi pengguna
    def describe_user(self):
        print("First name: " + self.first_name)
        print("Last name: " + self.last_name)
        print("Age: " + str(self.age))
        print("City: " + self.city)
        print("Username: " + self.username)
        
    # Memberikan sapaan kepada pengguna
    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome to python.")
        
# Membuat tiga object pengguna
user1 = User("Max", "Verstappen", 29, "Hasselt", "donatellomiaw")
user2 = User("Charles", "Leclerc", 29, "Monaco", "forzaferrari")
user3 = User("Carlos", "Sainz", 32, "Madrid", "chilliecrush")

# Menampilkan informasi dan sapaan pengguna pertama
user1.describe_user()
user1.greet_user()
print("=================================")

# Menampilkan informasi dan sapaan pengguna kedua
user2.describe_user()
user2.greet_user()
print("==================================")

# Menampilkan informasi dan sapaan pengguna ketiga
user3.describe_user()
user3.greet_user()
