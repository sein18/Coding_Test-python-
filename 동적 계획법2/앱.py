n, m = map(int, input().split())
mem = [*map(int, input().split())]
cost = [*map(int, input().split())]
k = 10001
d = [[0] * k for _ in range(n + 1)]
ans = 0

for i in range(n):
    x, c = mem[i], cost[i]
    for j in range(k):
        if (j >= c):
            d[i + 1][j] = max(d[i][j - c] + x, d[i][j])
        else:
            d[i + 1][j] = d[i][j]

for i in range(k):
    if (d[-1][i] >= m): ans = i; break

print(ans) 

