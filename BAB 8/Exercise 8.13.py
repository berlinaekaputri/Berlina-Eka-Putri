#Menulis fungsi menggunakan **kwargs, parameter yang menerima banyak argumen berbentuk key=value.
def build_profile(first, last, **user_info):
    profile = {
        'first_name': first,
        'last_name': last
    }

#Mengambil pasangan key dan value dari informasi tambahan.
    for key, value in user_info.items():
        profile[key] = value
        
    return profile

#Memanggil fungsi
my_profile = build_profile (
    "Berlina",
    "Eka putri",
    age = 19,
    major = "Industrial Engineering",
    hobby = "Cooking"
)

print(my_profile)