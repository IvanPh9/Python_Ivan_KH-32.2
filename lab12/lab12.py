import json
def Print(countries): #Друк словника
    for country, data in countries.items():
        string = f"Country {country}: Population {data['population']} million; Area {data['area']} thousand km²"
        print(string)

def update_json(countries, name):
    with open(name, "w") as file:
        json.dump(countries, file, indent=4)

def Del(countries, key): #Видалення за ключем
    if key in countries:
        del countries[key]
        string = f"Deleted {key}."
    else:
        string = f"Key '{key}' not found."
    print(string)
    update_json(countries, 'data.json')

def New(countries, key, population, area): #Додавання нового елементу списку
    if key in countries:
        string = f"Key '{key}' is already exists."
    else:
        countries[key] = {"population": population, "area": area}
        string = f"Added {key}: Population {population} million; Area {area} thousand km²"
    print(string)
    update_json(countries, 'data.json')

def Find(countries, key): #Пошук по ключу
    data = countries.get(key)  # Використовуємо .get() для безпечного доступу
    if data:
        print(f"Country {key}: Population {data['population']} million; Area {data['area']} thousand km²")
    else:
        print(f"Country {key} not found in the data.")

def max_density(countries):
    max_density = 0
    max_country = ""
    max_data = {}

    for country, data in countries.items():
        density = float(data['population']) / float(data['area'])
        if density > max_density:
            max_density = density
            max_country = country
            max_data = {country: {"population": data['population'], "area": data['area']}}

    # Записуємо дані країни з максимальною щільністю в JSON-файл
    if max_data:
        with open("data_1.json", "w") as file:
            json.dump(max_data, file, indent=4)

    print(f"\nCountry with the highest population density: {max_country} with a density of {max_density:.2f} million people per thousand km²")


try:
    with open("data.json", "r") as file:
        countries = json.load(file)
    n = True
    while (n): #Запит користувачу для виконання дій зі словником
        print("\nAvailable actions:")
        print("1: Print all countries")
        print("2: Add a new country")
        print("3: Delete a country")
        print("4: Find countries by name")
        print("5: Find the country with the highest population density")
        print("0: Exit")
        string = input()
        match string:
            case '0':
                n = False
            case '1':
                Print(countries)
            case '2':
                key = input("Country: ")
                population = float(input("Population (million): "))
                area = float(input("Area (thousand km²): "))
                New(countries, key, population, area)
            case '3':
                key = input("Country: ")
                Del(countries, key)
            case '4':
                key = input("Country: ")
                Find(countries, key)
            case '5':
                max_density(countries)
            case _:
                print("Task not found")
        print("-"*15)
except FileNotFoundError:
    print("Файл data.json не знайдено!")