import csv
import matplotlib.pyplot as plt
import numpy as np

# Список кольорів для графіків
colors = [
    "red",  # Червоний
    "steelblue",  # Синій
    "green",  # Зелений
    "yellow",  # Жовтий
    "purple",  # Фіолетовий
    "orange",  # Помаранчевий
    "pink",  # Рожевий
    "cyan",  # Бірюзовий
    "brown",  # Коричневий
    "magenta"  # Магента
]

try:
    # Відкриваємо CSV файл для читання
    with open("data.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        x = list(range(2013, 2024))  # Роки для графіку
        np.array(x)
        countrys = ["Ukraine", "United Kingdom"]  # Початкові країни для графіку
        i = 0

        # Створюємо фігуру з двома підграфіками
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

        # Перший підграфік для початкових країн
        for row in reader:
            if row['Country Name'] in countrys:
                y = []
                for year in x:
                    y.append(float(row[f"{year} [YR{year}]"]))  # Збираємо дані по роках
                np.array(y)
                ax1.plot(x, y, label=row['Country Name'], color=colors[i], linewidth=2,
                         marker='o')  # Малюємо лінію для кожної країни
                i += 1

        ax1.set_title('Inflation, consumer prices (annual %) - Initial Countries', fontsize=15,
                      family="Times New Roman")
        ax1.set_xlabel('Years', fontsize=14, color='navy', family="Times New Roman")
        ax1.set_ylabel('Inflation (%)', fontsize=14, color='navy', family="Times New Roman")
        ax1.legend()
        ax1.grid(True)

        # Скидаємо зчитування CSV файлу, щоб почати знову
        csvfile.seek(0)
        reader = csv.DictReader(csvfile, delimiter=",")

        i = 0
        countrys = []
        # Другий підграфік для додаткових країн як гістограма поруч
        print("Введіть країни, які бажаєте продемонстувати на графіку (або введіть 'exit' для завершення): ")
        while True:
            answer = str(input())  # Вводимо країни від користувача
            if answer.lower() == 'exit':
                break
            countrys.append(answer)

        bar_width = 0.8 / len(countrys)  # Ширина стовпчиків
        bar_positions = np.arange(len(x))  # Початкові позиції для стовпчиків
        country_offset = 0  # Зсув для забезпечення правильного розташування стовпчиків
        # Скидаємо зчитування CSV файлу для наступних країн
        csvfile.seek(0)
        reader = csv.DictReader(csvfile, delimiter=",")

        for row in reader:
            if row['Country Name'] in countrys:
                y = []
                valid_data = True  # Прапор для перевірки дійсності даних
                for year in x:
                    value = row[f"{year} [YR{year}]"]
                    if value == "..":  # Якщо дані недійсні (позначка '..'), пропускаємо країну
                        valid_data = False
                        break
                    y.append(float(value))
                if valid_data:  # Малюємо лише, якщо дані дійсні
                    np.array(y)
                    # Малюємо стовпчики для другого підграфіку, зсуваючи позиції
                    ax2.bar(bar_positions + country_offset, y, label=row['Country Name'], color=colors[i],
                            width=bar_width, alpha=0.7)
                    i += 1
                    country_offset += bar_width  # Збільшуємо зсув для наступних стовпчиків
        ax2.set_title('Inflation, consumer prices (annual %) - User Selected Countries (Histogram)', fontsize=15,
                      family="Times New Roman")
        ax2.set_xlabel('Years', fontsize=14, color='navy', family="Times New Roman")
        ax2.set_ylabel('Inflation (%)', fontsize=14, color='navy', family="Times New Roman")
        ax2.set_xticks(
            bar_positions + bar_width * (i / len(countrys)))  # Позиціюємо підписи до осі X по центру стовпчиків
        ax2.set_xticklabels(x)
        ax2.legend()
        ax2.grid(True)

        # Виводимо обидва графіки в одній фігурі
        plt.tight_layout()
        plt.show()

except FileNotFoundError:
    print("Файл data.csv не знайдено!")  # Повідомлення про помилку, якщо файл не знайдений
