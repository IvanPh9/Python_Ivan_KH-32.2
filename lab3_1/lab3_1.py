string = input("Введіть слово: ")

while not string.isalpha() or " " in string or len(string) < 3:
    print("Лише одне слово без цифр з кількістю літер більшу за 3:")
    string = input("Спробуйте ще раз: ")

string_1 = string[2::3]

print("Кожна третя буква слова:", string_1)
