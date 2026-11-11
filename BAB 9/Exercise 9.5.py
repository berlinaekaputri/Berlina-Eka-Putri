# Mendefinisikan bentuk Class 
class User:  
# Menentukan atribut pengguna
    def __init__(self, first_name, last_name, age, city, username):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.username = username
        self.login_attempts = 0
        
    #Menambahkan jumlah percobaan login
    def increment_login_attempts(self):
        self.login_attempts += 1
        
        # Mengatur ulang jumlah percobaan login
    def reset_login_attempts(self):
        self.login_attempts = 0

# Membuat object User
user = User("Max", "Verstappen", 29, "Hasselt", "simplylovliey")

# Menambahkan percobaan login sebanyak tiga kali
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Menampilkan jumlah percobaan login
print("Login attempts:", user.login_attempts)

# Mengatur ulang jumlah percobaan login
user.reset_login_attempts()

# Menampilkan jumlah percobaan login setelah direset
print("Login attempts after reset:", user.login_attempts)
