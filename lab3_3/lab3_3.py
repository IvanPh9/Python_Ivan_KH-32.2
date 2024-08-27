print("Введіть речення:")
string = input()
word = ""
words = []
punctuation = " ,.!?:-"

for i in range(len(string)):
    if string[i] not in punctuation:
        word += string[i]
    else:
        if word:
            if word in words:
                print("Слово, що повторюється два рази:",word)
                exit(0)
            words.append(word)
            word = ""

if word and word in words:
    print("Слово, що повторюється два рази:",word)
else:
    print("Не виявлено повторів слів")
