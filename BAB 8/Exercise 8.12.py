#Menulis fungsi menggunakan *args, parameter yang bisa menerima banyak argumen.
def make_sandwich(*items):
    print("Your sandwich order:")
    for item in items:
        print("- " + item)

#Memanggil fungsi
make_sandwich("cheese", "lettuce")
print("=================================")

make_sandwich("chicken", "tomato", "cheese")
print("=================================")

make_sandwich("beef", "egg", "lettuce", "mayonnaise")
print("=================================")