n = 7
a = [[1*(i == 0 or j == 0 or i == n-1 or j == n-1) for i in range(n)] for j in range(n)]
for r in a:
        print(*r)