def new():
    A = list(map(int,input('Введіть список елементів: ').split()))
    print(A)
    result = []
    for x in range(2, len(A), 3):
        result.append(A[x])
    print(result)
    return result
new()