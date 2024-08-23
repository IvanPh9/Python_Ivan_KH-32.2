numbers = [1, 3, 5, 9, 17]
print("N", "N^2", "N^3", sep='\t'*2)
print("▪"*22)
for x in numbers:
    squares = x**2
    cubes = x**3
    print(x, squares, cubes, sep='\t'*2)
