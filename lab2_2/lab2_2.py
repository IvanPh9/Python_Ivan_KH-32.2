from file_z import factorial
N = int(input("Введіть число для обрахуванння факторіалу: "))
while N < 0:
    N = int(input("Повторно ведіть число для обрахуванння факторіалу, більше 0: "))
print("Z =", factorial(N))