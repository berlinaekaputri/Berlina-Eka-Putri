sandwich_orders = ["Tuna", "Pastrami", "Beef", "Pastrami", "Cheese", "Pastrami", "Chicken", "Egg"]
finished_sandwich = []

print("The Deli has run out off Pastrami. \n")
#Menghapus pastrami dari sandwich_orders
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
    
#Memastikan bahwa pastrami sudah tidak ada 
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich")
    finished_sandwich.append(current_sandwich)
    
print("\nThe following sandwiches have been made:")

for sandwich in finished_sandwich:
    print(sandwich)