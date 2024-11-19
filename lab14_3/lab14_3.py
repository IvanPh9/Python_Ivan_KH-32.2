import matplotlib.pyplot as plt
import numpy as np

countries = {"Ukraine": {"population": 41, "area": 603.7},
             "France": {"population": 67.5, "area": 551.5},
             "Germany": {"population": 83.2, "area": 357.4},
             "Italy": {"population": 60.4, "area": 301.3},
             "Spain": {"population": 47.4, "area": 505.9},
             "Poland": {"population": 38.2, "area": 312.7},
             "Romania": {"population": 19, "area": 238.4},
             "Czechia": {"population": 10.7, "area": 78.9},
             "Sweden": {"population": 10.4, "area": 450.3},
             "Portugal": {"population": 10.3, "area": 92.2}}

x = []
population = []
area = []

for country in countries:
    x.append(country)
    population.append(countries[country]["population"])
    area.append(countries[country]["area"])

# Преобразуємо у numpy масиви
x = np.array(x)
population = np.array(population)
area = np.array(area)

# Створюємо два графіки
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Графік для населення
ax1.pie(population, labels=x, autopct='%1.1f%%', startangle=90)
ax1.axis("equal")  # Кругла форма
ax1.set_title("Населення країн")

# Графік для території
ax2.pie(area, labels=x, autopct='%1.1f%%', startangle=90)
ax2.axis("equal")  # Кругла форма
ax2.set_title("Територія країн")

# Показуємо графіки
ax1.legend()
ax2.legend()
plt.show()