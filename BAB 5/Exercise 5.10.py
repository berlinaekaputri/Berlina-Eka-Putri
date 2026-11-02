current_users = ["Alex", "Nikola", "Britney", "Neil", "Leo"]
new_users = ["Arvid", "Yuki", "NIKOLA", "Isack", "max"]

#Mengubah current users menjadi huruf kecil semua
current_users_lower = [user.lower() for user in current_users]

# Memeriksa username baru
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, {new_user} is already taken. Please enter a new username.")
    else:
        print(f"{new_user} is available.")