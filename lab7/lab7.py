def Print(countries): #Друк словника
    for country, data in countries.items():
        string = f"Country {country}: Population {data['population']} million; Area {data['area']} thousand km²"
        print(string)

def Del(countries, key): #Видалення за ключем
    if key in countries:
        del countries[key]
        string = f"Deleted {key}."
    else:
        string = f"Key '{key}' not found."
    print(string)

def New(countries, key, population, area): #Додавання нового елементу списку
    if key in countries:
        string = f"Key '{key}' is already exists."
    else:
        countries[key] = {"population": population, "area": area}
        string = f"Added {key}: Population {population} million; Area {area} thousand km²"
    print(string)

def Sort(countries): #Сортування по ключу
    countries = {k: countries[k] for k in sorted(countries)}
    print("Sorted successfully")
    Print(countries)

def Max_Density(countries): # Пошук максимального значення щільності
    max_density = 0
    max_country = ""
    for country, data in countries.items():
        density = float(data['population']) / float(data['area'])
        if density > max_density:
            max_density = density
            max_country = country
    if max_country:
        print(f"\nCountry with the highest population density: {max_country} with a density of {max_density:.2f} million people per thousand km²")

countries = {
    "Ukraine": {"population": 41.0, "area": 603.7},
    "France": {"population": 67.5, "area": 551.5},
    "Germany": {"population": 83.2, "area": 357.4},
    "Italy": {"population": 60.4, "area": 301.3},
    "Spain": {"population": 47.4, "area": 505.9},
    "Poland": {"population": 38.2, "area": 312.7},
    "Romania": {"population": 19.0, "area": 238.4},
    "Czechia": {"population": 10.7, "area": 78.9},
    "Sweden": {"population": 10.4, "area": 450.3},
    "Portugal": {"population": 10.3, "area": 92.2}
}
n = True
while (n): #Запит користувачу для виконання дій зі словником
    print("\nAvailable actions:")
    print("1: Print all countries")
    print("2: Add a new country")
    print("3: Delete a country")
    print("4: Sort countries by name")
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
            population = input("Population (million): ")
            area = input("Area (thousand km²): ")
            New(countries, key, population, area)
        case '3':
            key = input("Country: ")
            Del(countries, key)
        case '4':
            Sort(countries)
        case '5':
            Max_Density(countries)
        case _:
            print("Task not found")
    print("-"*15)