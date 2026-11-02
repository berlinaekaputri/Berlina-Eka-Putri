usernames = ["Alex", "Nikola", "Britney", "Admin", "Leo"]
for username in usernames:
    if username == "Admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")