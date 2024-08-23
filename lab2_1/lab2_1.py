def z_function(x, y):
    z = 0
    if x > 8: z = 3 + y
    else: z = 9 * x * y
    return z

def factorial(n):
    Z = 1
    for i in range(n, 0, -1):
        Z *= i
    return Z

X = float(input("Введіть x: "))
Y = float(input("Введіть y: "))
print("z =", z_function(X, Y))

N = int(input("Введіть число для обрахування факторіалу: "))
while N < 0:
    N = int(input("Повторно ведіть число для обрахування факторіалу, більше 0: "))
print("Z =", factorial(N))
