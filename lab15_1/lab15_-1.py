import pandas as pd

def categorize(density):
    if density <= 0.1: return "Low"
    elif density <= 0.2: return "Medium"
    else: return "High"

# Введені дані про країни
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

# Створення DataFrame
data_f = pd.DataFrame(countries).T  # Використовуємо .T для транспонування таблиці

# Розрахунок щільності населення для кожної країни
data_f['density'] = data_f['population'] / data_f['area']

data_f['density_category'] = data_f['density'].apply(categorize)

print(data_f, "\n")

# Використання функції агрегації для обчислення статистичних даних
aggregated_data = data_f.agg({
    'population': ['sum', 'mean', 'min', 'max'],
    'area': ['sum', 'mean', 'min', 'max'],
    'density': ['mean', 'min', 'max']
})

grouped_data = data_f.groupby('density_category').mean()

# Виведення результатів агрегації
print("\nАгреговані дані:")
print(aggregated_data)

print("\nГруповані дані (середнє значення):")
print(grouped_data)