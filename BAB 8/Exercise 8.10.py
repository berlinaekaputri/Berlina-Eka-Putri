#Menuliskan fungsi
def send_messages(messages, sent_messages):
#Memindahkan pesan
    for message in messages:
        print(message)
        sent_messages.append(message)
   
#Membuat list sebagai argumen ke fungsi     
messages = [
    "Hello, apa kabar?",
    "Apakah kamu sudah makan?",
    "Semangat belajar python!",
    "Jaga kesehatan ya!"
]

sent_messages = []

#Memanggil fungsi
send_messages(messages, sent_messages)

print("=================================")
 
print("Original messages:")
print(messages)

print("=================================")

print("Sent messages:")
print(sent_messages)