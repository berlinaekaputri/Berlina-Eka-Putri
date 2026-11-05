#Menulis Fungsi
def describe_city(city, country = "Italia"):
    print(f"{city} is in {country}.")
 
#Memanggil fungsi secara default dan berbeda   
describe_city("Sisilia")
describe_city("Crema")
describe_city("Tokyo", "Jepang")