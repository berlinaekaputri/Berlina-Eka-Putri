#Different version Exercise 7.4

#conditional test in the while statement to stop the loop
#Meminta user untuk memasukkan data topping
topping = input("Enter a topping: ")

#Membuat perulangan setelah user memasukkan data yang sesuai
while topping != 'quit':
    print(f"I'll add {topping} to your pizza.")
    topping = input("Enter a topping: ")

print("============================================================")

#Active variable
active = True

#Membuat perulangan input untuk user agar dapat memasukkan data topping
while active:
    topping = input("Enter a topping: ")

#Apabila input yang dimasukkan adalah 'quit' maka program berhenti
    if topping == 'quit':
        active = False
#Apabila input yang dimasukkan benar yaitu tentang topping pizza
    else:
        print(f"I'll add {topping} to your pizza.")
        
print("============================================================")

#Break statement
#Meminta user memasukkan data topping
while True:
    topping = input("Enter a topping: ")

#Apabila input yang dimasukkan adalah 'quit' maka program selesai
    if topping == 'quit':
        break

    print(f"I'll add {topping} to your pizza.")