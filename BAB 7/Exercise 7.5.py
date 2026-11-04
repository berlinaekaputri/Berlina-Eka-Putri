while True:
    age = int(input("Please enter your age = "))
    
    if age < 3:
        print("Your ticket is free")
    elif age in range (3, 12):
        print("Your ticket is $10")
    elif age > 12:
        print("Your ticket is $15")
    