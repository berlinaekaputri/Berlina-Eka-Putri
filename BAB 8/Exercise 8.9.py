#Menulis fungsi
def show_messages(messages):
    for message in messages:
        print(message)

#Membuat list sebagai argumen ke fungsi
messages = [
    "Hello, apa kabar?",
    "Apakah kamu sudah makan?",
    "Semangat belajar python!",
    "Jaga kesehatan ya!"
]

#Memanggil fungsi
show_messages(messages)