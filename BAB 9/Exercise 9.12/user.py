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
        print("Hello, " + self.first_name + "! Welcome back.")