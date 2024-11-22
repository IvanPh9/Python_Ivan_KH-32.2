import nltk
from nltk.corpus import stopwords
import string
import matplotlib.pyplot as plt
from collections import Counter

# Функція для візуалізації 10 найбільш вживаних слів у тексті
def most_used_words(text):
    cnt = Counter(text)  # Рахуємо кількість повторень кожного слова
    cort = cnt.most_common(10)  # Беремо 10 найбільш вживаних слів

    # Створюємо списки слів та їх частот
    x = [cort[e][0] for e in range(len(cort))]  # Слова
    y = [cort[e][1] for e in range(len(cort))]  # Кількість повторень

    # Побудова графіку
    plt.bar(x, y)
    plt.title("10 найбільш вживаних слів у тексті", fontsize=16, color='navy', family="Times New Roman")
    plt.xlabel("Слова", fontsize=14, color='navy', family="Times New Roman")
    plt.ylabel("Зустрічаються разів у тексті", fontsize=14, color='navy', family="Times New Roman")
    plt.show()

# Перевірка відкриття файлу для читання
try:
    File = open('shakespeare-caesar.txt', 'r', encoding='utf-8')
except FileNotFoundError:
    print("Файл не знайдено!")
    exit(0)

text = File.read()  # Зчитуємо текст з файлу

# Аналіз початкового тексту без обробки
st_text = text.split()  # Розділення тексту на окремі слова
most_used_words(st_text)

# Завантажуємо список стоп-слів англійською
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))  # Список стоп-слів

# Очищення тексту від стоп-слів та пунктуації
text_sp = text.split()  # Розділення тексту на окремі слова
fn_text = [word.strip(string.punctuation) for word in text_sp if word.strip(string.punctuation).lower() not in stop_words] # Видаляємо пунктуацію та фільтруємо слова, які є стоп-словами

most_used_words(fn_text)
