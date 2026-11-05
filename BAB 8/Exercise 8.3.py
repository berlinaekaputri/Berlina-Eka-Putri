#Menulis fungsi
def make_shirt(size, message):
    print(f"The shirt size is {size} and the message printed on it is {message}.")

#Memanggil fungsi dengan Positional arguments
make_shirt("XL", "I love New York")

#Memanggil fungsi dengan keyword arguments
make_shirt(size = "L", message = "I love BALI")