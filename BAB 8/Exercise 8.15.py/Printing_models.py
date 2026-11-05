# Mengimpor fungsi dari file printing_functions.py
import Printing_Function
# Membuat daftar model yang belum dicetak
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']

# Membuat daftar kosong untuk model yang sudah dicetak
completed_models = []

# Memanggil fungsi print_models dari modul printing_functions
Printing_Function.print_models(
    unprinted_designs, completed_models
)

# Memanggil fungsi show_completed_models
Printing_Function.show_completed_models(completed_models)