#Menulis fungsi menggunakan **kwargs, parameter yang menerima banyak argumen berbentuk key=value.
def make_car(manufacturer, model, **car_info):
    car = {
        'manufacturer': manufacturer,
        'model': model
    }

#Mengambil pasangan key dan value dari informasi tambahan.
    for key, value in car_info.items():
        car[key] = value

    return car

#Memanggil function
car = make_car(
    'subaru',
    'outback',
    color = 'blue',
    tow_package = True
)

print(car)