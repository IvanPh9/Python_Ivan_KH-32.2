number = str(input("Введіть шестизначне натуральне число: "))
while not len(number) == 6 or number.isdigit() == 0:
    number = str(input("Введіть число ще раз, так як воно не шестизначне або це не число: "))
sum = 0
for i in range (len(number)):
    sum += int(number[i])
print("Сума усіх цифр у шестизначному числі = ", sum)