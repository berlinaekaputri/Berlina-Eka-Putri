rivers = {
    "Nil" : "Mesir",
    "Amazon" : "Brazil",
    "Yangtze" : "China"
}

# Menampilkan kalimat tentang sungai dan negara
for river, country in rivers.items():
    print(f"sungai {river.title()} terletak di negara {country.title()}.")

print("===================================================")

#Menampilkan nama sungai
print("Nama sungai:")
for river in rivers.keys():
    print(river.title())
    
print("===================================================")   
    
#Menampilkan nama negara
print("Nama negara:")
for country in rivers.values():
    print(country.title())
