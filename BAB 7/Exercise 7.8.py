sandwich_orders = ["Tuna", "Beef", "Cheese", "Chicken", "Egg"]
finshed_sandwich = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    print(f"I made your {current_sandwich} sandwich")
    finshed_sandwich.append(current_sandwich)

print("\nThe following sandwiches have been made:")

for sandwich in finshed_sandwich:
    print(sandwich)