#Menulis fungsi secara default
def make_shirt(size="large", message= "I love Python"):
    print(f"The shirt size is {size} and the message is {message}.")

# Memanggil fungsi secara default
make_shirt()

#Memanggil fungsi dengan pesan default
make_shirt(size="medium")

#Memanggil fungsi dengan ukuran dan pesan yang berbeda
make_shirt(size="small", message="I LOVE U")