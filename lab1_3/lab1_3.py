while True:
    try:
        n = int(input("Введіть висоту пірамідки - "))
        if n <= 0 or n >= 9:
            print("Висота не підлягає діапазону (0<n<9)")
        else:
            break
    except ValueError:
        print("Невірний тип розміру пірамідки")

strings = ''
for i in range(n-1, -1, -1):
    strings += ' ' * (i*2) + ' '.join(str(j) for j in range(i+1, n+1))  + '\n'
print(strings)