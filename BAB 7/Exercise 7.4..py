#Meminta user untuk menginput topping pizza
topping = input("Enter a pizza topping: ")

#Membuat perulangan apabila user memasukkan data tentang topping pizza
while topping != 'quit':
    print(f"I'll add {topping} to your pizza.")
    topping = input("Enter a pizza topping: ")
    