a= int(input ("Введіть а: "))
while (a < 1 or a > 100):
    a = int(input ("Введіть  ще раз а: "))
b = int(input ("Введіть b: "))
while (b < 1 or b > 100):
    b = int(input ("Введіть ще раз b: "))
if a < b:
    X = (a * 3 - 5)/b
elif a > b:
    X = (a**4 + b)/a
else:
    X = -4
print("Результат обчислення Х =", X)
