def print_models(unprinted_designs, completed_models):

    # Mengulang selama masih ada model yang belum dicetak
    while unprinted_designs:

        # Mengambil model terakhir dari daftar
        current_design = unprinted_designs.pop()

        # Menampilkan model yang sedang dicetak
        print("Printing model: " + current_design)

        # Memindahkan model ke daftar yang sudah selesai
        completed_models.append(current_design)


# menampilkan semua model yang sudah dicetak
def show_completed_models(completed_models):

    # Menampilkan judul
    print("\nThe following models have been printed:")

    # Menampilkan setiap model
    for completed_model in completed_models:
        print(completed_model)