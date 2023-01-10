n = int(input())
d = [[0] * 10 for _ in range(n+1)]
mod = 10 ** 9

for i in range(1, 10):
    d[1][i] = 1

for i in range(1, n):
    d[i+1][0] = d[i][1]
    d[i+1][9] = d[i][8]
    for j in range(1, 9):
        d[i+1][j] = d[i][(j+1) % 10] + d[i][(j+9) % 10]

print(sum(d[ - 1]) % mod) 