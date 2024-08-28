print("Введіть речення:")
string = input()

punctuation = ".,!?-:;"
for char in punctuation:
    string = string.replace(char, '')

words = string.split()

for word in words:
    if words.count(word) > 1:
        print("Слово, що повторюється два рази:",word)
        exit(0)

print("Не виявлено повторів слів")
