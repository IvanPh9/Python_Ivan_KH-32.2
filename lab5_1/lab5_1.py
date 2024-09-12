n = int(input("n = "))
while n < 2:
    n = int(input("Введіть n > 1 = "))
print(f"Введіть {n} елементів масиву(списку):")

arr = [float(input()) for _ in range(n)]
print("Початковий масив: ", *arr)

mass = [x for x in reversed(arr) if x != 0]
print("Ненульові елементи в зворотньому порядку:", *mass)
