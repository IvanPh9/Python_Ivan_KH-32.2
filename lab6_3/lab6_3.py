def search():
    A = input("Ваш текст латинецею: ")
    B = A.lower()
    print("Текст:", B)

    g_count = sum(B.count(char) for char in set(B) & set('aeiouy'))
    p_count = sum(B.count(char) for char in set(B) & set('bcdfghjklmnpqrstvwxz'))

    print(f"Кількість голосних: {g_count}")
    print(f"Кількість приголосних: {p_count}")

    if g_count > p_count:
        print("Більше голосних")
    elif p_count > g_count:
        print("Більше приголосних")
    else:
        print("Однакова кількість голосних та приголосних")

search()
