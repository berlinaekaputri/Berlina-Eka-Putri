nama_pembalap = "Max Verstappen"
kewarganegaraan = "Belanda"
tim = "Red Bull"
umur = 28
nomor_punggung = 3


pembalap_f1 = ["Max Verstappen", "Charles Leclerc", "Oscar Piastri", "Carlos Sainz", "Arvid Linbald"]

#Equality and Inequality
print("Equality:")
print(nama_pembalap == "Max Verstappen")

print("Inequality:")
print(nama_pembalap != "Charles Leclerc")

print("=================================")

#Tests using lower() method
print("Lower method:")
print(tim.lower() == 'red bull')
print(tim.lower() == 'Red Bull')

print("=================================")

#Numerical Tests
print("Numerical Tests:")
print(umur == 28)
print(umur != 30)
print(umur > 25)
print(umur < 30)
print(umur >= 28)
print(umur <= 28)

print("=================================")

#Tests using AND and OR
print("AND Tests:")
print(umur > 20 and tim == "Red Bull")
print(umur < 20 and tim == "Red Bull")

print()

print("OR Tests:")
print(umur > 30 or tim == "Red Bull")
print(umur < 20 or tim == "Red Bull")

print("=================================")


#Test whether an item is in a list
print("In List:")
print('Max Verstappen' in pembalap_f1)
print('Carlos Sainz' in pembalap_f1)

print("=================================")

#Test whether an item is not in a list
print("Not in List:")
print('Carlos Sainz' not in pembalap_f1)
print('Charles Leclerc' not in pembalap_f1)
