def factorial(n):
    Z = 1
    for i in range(n, 0, -1):
        Z *= i
    return Z