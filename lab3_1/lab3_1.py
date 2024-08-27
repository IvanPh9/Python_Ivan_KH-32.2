string = input("Введіть слово: ")
string_1 = ""

while not string.isalpha() or " " in string or len(string) < 3:
    print("Лише одне слово без цифр з кількістю літер більшу за 3:")
    string = input("Спробуйте ще раз: ")
print("Кількість літер у слові:",len(string))
for i in range(2, len(string), 3):
    string_1 += string[i]
print("Кожна третя буква слова: ",string_1)
