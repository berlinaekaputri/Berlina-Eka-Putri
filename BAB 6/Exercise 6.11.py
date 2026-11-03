cities = {
    'surakarta': {
        'country': 'Indonesia',
        'population': '522,364',
        'fact': 'Kota penghasil kain batik'
    },

    'tokyo': {
        'country': 'Japan',
        'population': '14 million',
        'fact': 'Memiliki stasiun bawah tanah tersibuk di dunia'
    },

    'paris': {
        'country': 'France',
        'population': '2.1 million',
        'fact': 'Memiliki menara yang terkenal yaitu Eifell tower'
    }
}

for city, information in cities.items():
    print("City:", city.title())
    print("Country:", information['country'])
    print("Population:", information['population'])
    print("Fact:", information['fact'])
    print("===========================================")