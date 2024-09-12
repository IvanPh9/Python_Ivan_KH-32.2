def delete():
    A = list(map(int,input('Введіть список елементів: ').split()))
    print(A)
    k = int(input('Введіть значення для видалення: '))
    result = []
    for x in range(len(A)):
        if A[x] != k:
            result.append(A[x])
    print(result)
    return result
delete()