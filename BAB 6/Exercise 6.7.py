person1 = {
    "first_name" : "Max",
    "last_name" : "Verstappen",
    "age" : 29,
    "city" : "Hasselt"
}

person2 = {
    "first_name" : "Charles",
    "last_name" : "Leclerc",
    "age" : 29,
    "city" : "Monte Carlo"
}

person3 = {
    "first_name" : "Oscar",
    "last_name" : "Piastri",
    "age" : 26,
    "city" : "Sydney"
}

people = [person1, person2, person3]

for person in people:
    print("First Name:", person['first_name'])
    print("Last Name:", person['last_name'])
    print("Age:", person['age'])
    print("City:", person['city'])
    print("================================")