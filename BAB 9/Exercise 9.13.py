import random #Untuk menghasilkan sesuatu secara acak

class Die:
    def __init__(self, sides=6):
        self.sides = sides #Self merujuk pada objek yang dibuat
    
    # Method untuk melempar dadu
    def roll_die(self):
        print(random.randint(1, self.sides))
        
# Membuat dadu dengan 6 sisi
print("Rolling a 6-sided die:")
die_6 = Die() #Jika tidak diberi angka maka nilainya akan mengikuti default yaitu 6

for roll in range(10):
    die_6.roll_die()


# Membuat dadu dengan 10 sisi
print("\nRolling a 10-sided die:")
die_10 = Die(10)

for roll in range(10):
    die_10.roll_die()


# Membuat dadu dengan 20 sisi
print("\nRolling a 20-sided die:")
die_20 = Die(20)

for roll in range(10):
    die_20.roll_die()