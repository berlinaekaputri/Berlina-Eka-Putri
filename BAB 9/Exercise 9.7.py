#Mendefinisikan bentuk Class 
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

class Admin(User):
    
    # Menentukan atribut administrator
    def __init__(self, first_name, last_name, age, city, username):
        super().__init__(first_name, last_name, age, city, username)
        self.privileges = [
        "can add post",
        "can delete post",
        "can ban user"
    ]  
     # Menampilkan method hak akses administrator
    def show_privileges(self) :
        print("Administrator privileges:")

        for privilege in self.privileges:
            print(privilege)

# Membuat object Admin
admin = Admin("Max", "Verstappen", 29, "Hasselt", "simplylovliey")

# Menampilkan hak akses administrator
admin.show_privileges()

