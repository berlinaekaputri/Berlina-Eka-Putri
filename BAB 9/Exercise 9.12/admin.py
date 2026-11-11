from user import User

# Membuat class Privileges
class Privileges:

    # Menentukan atribut hak akses
    def __init__(self):
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user"
        ]

    # Menampilkan hak akses administrator
    def show_privileges(self):
        print("Administrator privileges:")

        for privilege in self.privileges:
            print(privilege)
            
# Membuat child class Admin
class Admin(User):

    # Menentukan atribut administrator
    def __init__(self, first_name, last_name, age, city, username):
        super().__init__(first_name, last_name, age, city, username)
        self.privileges = Privileges()
