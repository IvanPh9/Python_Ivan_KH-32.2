import pandas as pd

import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)

def Month_ct(Date):
    return Date.month

try:
    # Завантаження даних
    fixed_df = pd.read_csv('data.csv', sep=',', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
    fixed_df = fixed_df.drop('Time', axis=1)
    # Перегляд перших трьох рядків
    print(fixed_df[:3])
    # Побудова графіку

    # Створення стовпця з місяцями
    fixed_df['Month'] = fixed_df.index.to_series().apply(Month_ct)
    # Групування за місяцями та підсумок
    grouped_data = fixed_df.groupby('Month').sum()
    # Додавання стовпця з сумою всіх стовпців, крім першого
    grouped_data['Sum'] = grouped_data.iloc[:, 1:].sum(axis=1)
    print(grouped_data)

    # Визначення місяця з найбільшою популярністю (максимальною сумою)
    most_popular_month = grouped_data['Sum'].idxmax()
    print(f"Місяць, який є найбільш популярним серед велосипедистів: {most_popular_month}")
    grouped_data['Sum'].plot(figsize=(15, 10), marker="o")
    plt.legend()
    plt.title('Загальне відвідування велодоріжок за місяці 2017 року', fontsize=15, family="Times New Roman")
    plt.xlabel('Місяць', fontsize=14, color='navy', family="Times New Roman")  # позначення вісі абсцис
    plt.ylabel('Сума всіх відвідувань', fontsize=14, color='navy', family="Times New Roman")
    plt.show()
except FileNotFoundError:
    print("Помилка: Файл 'data.csv' не знайдено.")



