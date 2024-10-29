import csv
from prettytable import PrettyTable

try:
    with open("Data_1.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        table = PrettyTable()
        table.field_names = ["Country Name", "2018", "2019"]
        print("Inflation, consumer prices (annual %):")
        for row in reader:
            if row["2018 [YR2018]"] != ".." and row["2019 [YR2019]"] != "..":
                year_2018 = f"{float(row['2018 [YR2018]']):.3f}"
                year_2019 = f"{float(row['2019 [YR2019]']):.3f}"
                table.add_row([row['Country Name'], year_2018, year_2019])
        print(table)

except FileNotFoundError:
    print("Файл Data_1.csv не знайдено!")

try:
    with open("Data_1.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        print("Введіть країни для пошуку (натисніть 0 для завершення вводу):")
        database = []
        countrys = []

        while True:
            choice = input()
            if choice == "0":
                break
            countrys.append(choice)

        for row in reader:
            if row['Country Name'] in countrys:
                database.append(row)
        with open("Data_2.csv", "w") as csvfile2:
            writer = csv.writer(csvfile2, delimiter=",")
            writer.writerow(("Country Name","2018 [YR2018]", "2019 [YR2019]"))
        table = PrettyTable()
        table.field_names = ["Country Name", "2018", "2019"]
        for row in database:
            if row["2018 [YR2018]"] != ".." and row["2019 [YR2019]"] != "..":
                year_2018 = f"{float(row['2018 [YR2018]']):.3f}"
                year_2019 = f"{float(row['2019 [YR2019]']):.3f}"
                table.add_row([row['Country Name'], year_2018, year_2019])
                with open("Data_2.csv", "a") as csvfile2:
                    writer = csv.writer(csvfile2, delimiter=",")
                    writer.writerow((row["Country Name"], row["2018 [YR2018]"], row["2019 [YR2019]"]))
        print(table)

except FileNotFoundError:
    print("Файл Data_1.csv не знайдено!")
