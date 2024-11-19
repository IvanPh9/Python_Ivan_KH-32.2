import csv
import matplotlib.pyplot as plt
import numpy as np

colors = [
    "red",         # Червоний
    "steelblue",        # Синій
    "green",       # Зелений
    "yellow",      # Жовтий
    "purple",      # Фіолетовий
    "orange",      # Помаранчевий
    "pink",        # Рожевий
    "cyan",        # Бірюзовий
    "brown",       # Коричневий
    "magenta"      # Магента
]

try:
    with open("data.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        x = list(range(2013, 2024))
        np.array(x)
        countrys = ["Ukraine", "United Kingdom"]
        i = 0

        # Create a figure with 2 subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

        # First subplot for the initial countries
        for row in reader:
            if row['Country Name'] in countrys:
                y = []
                for year in x:
                    y.append(float(row[f"{year} [YR{year}]"]))
                np.array(y)
                ax1.plot(x, y, label=row['Country Name'], color=colors[i], linewidth=2, marker='o')
                i += 1

        ax1.set_title('Inflation, consumer prices (annual %) - Initial Countries', fontsize=15, family="Times New Roman")
        ax1.set_xlabel('Years', fontsize=14, color='navy', family="Times New Roman")
        ax1.set_ylabel('Inflation (%)', fontsize=14, color='navy', family="Times New Roman")
        ax1.legend()
        ax1.grid(True)

        # Reset CSV file reading to start from the beginning again
        csvfile.seek(0)
        reader = csv.DictReader(csvfile, delimiter=",")

        i = 0
        countrys = []
        # Second subplot for additional countries as histogram side by side
        print("Введіть країни, які бажаєте продемонстувати на графіку (або введіть 'exit' для завершення): ")
        while True:

            answer = str(input())
            if answer.lower() == 'exit':
                break
            countrys.append(answer)

        bar_width = 0.8 / len(countrys) # Width of the bars
        bar_positions = np.arange(len(x))  # Initial x positions for the bars
        country_offset = 0  # Offset to ensure bars are plotted side by side
        # Reset CSV file reading for the next country
        csvfile.seek(0)
        reader = csv.DictReader(csvfile, delimiter=",")
        for row in reader:
            if row['Country Name'] in countrys:
                y = []
                valid_data = True  # Flag to check if data is valid
                for year in x:
                    value = row[f"{year} [YR{year}]"]
                    if value == "..":
                        valid_data = False  # Mark data as invalid if any year has '..'
                        break
                    y.append(float(value))
                if valid_data:  # Only plot if data is valid
                    np.array(y)
                    # Plot bars for the second subplot, shifting positions
                    ax2.bar(bar_positions + country_offset, y, label=row['Country Name'], color=colors[i],
                            width=bar_width, alpha=0.7)
                    i += 1
                    country_offset += bar_width  # Increment the offset to plot the next country's bars
        ax2.set_title('Inflation, consumer prices (annual %) - User Selected Countries (Histogram)', fontsize=15, family="Times New Roman")
        ax2.set_xlabel('Years', fontsize=14, color='navy', family="Times New Roman")
        ax2.set_ylabel('Inflation (%)', fontsize=14, color='navy', family="Times New Roman")
        ax2.set_xticks(bar_positions + bar_width * (i / len(countrys)))  # Position xticks in the center of the grouped bars
        ax2.set_xticklabels(x)
        ax2.legend()
        ax2.grid(True)

        # Show both subplots in the same window
        plt.tight_layout()
        plt.show()
except FileNotFoundError:
    print("Файл data.csv не знайдено!")
