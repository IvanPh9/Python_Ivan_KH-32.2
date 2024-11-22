import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import string
import re

# Завантаження необхідних ресурсів
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')

# Перевірка відкриття файлу для читання
try:
    File = open('text.txt', 'r', encoding='utf-8')
except FileNotFoundError:
    print("Файл не знайдено!")
    exit(0)

text = File.read()  # Зчитуємо текст з файлу
File.close()  # Закриваємо файл після зчитування

# Токенізація тексту
text_new = word_tokenize(text)
print("Токенізований текст:", text_new)

# Стемінг слів у тексті
ps = PorterStemmer()
text_new = [ps.stem(w) for w in text_new]  # Створення нового списку зі стемінгом
print("Текст після стемінгу:", text_new)

# Лематизація слів у тексті
wordnet_lemmatizer = WordNetLemmatizer()
text_new = [wordnet_lemmatizer.lemmatize(w) for w in text_new]
print("Текст після лематизації:", text_new)

# Видаляємо пунктуацію та фільтруємо стоп-слова
stop_words = set(stopwords.words('english'))
text_new = [word.strip(string.punctuation) for word in text_new if word.strip(string.punctuation).lower() not in stop_words]
print("Текст після видалення стоп-слів:", text_new)

# Видаляємо залишкові знаки пунктуації
text_new = [x for x in text_new if not re.fullmatch('[' + string.punctuation + ']+', x)]
print("Фінальний текст без знаків пунктуації:", text_new)

# Запис обробленого тексту у новий файл
try:
    with open('text_new.txt', 'w', encoding='utf-8') as File:
        File.write(' '.join(text_new))  # Об'єднання списку слів у рядок з пробілами
except FileNotFoundError:
    print("Файл не знайдено!")
    exit(0)
