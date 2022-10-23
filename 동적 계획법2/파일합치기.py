t = int(input())

for tc in range(t):
    k = int(input())
    a = [0] + [*map(int, input().split())]
    inf = 10 ** 9
    d = [[inf] * (k + 1) for _ in range(k + 1)]
    s = [0] * (k + 1)
    for i in range(1, k):
        d[i][i] = 0
        d[i][i + 1] = a[i] + a[i + 1]
        s[i] = s[i - 1] + a[i]
    d[k][k] = 0
    s[k] = s[k - 1] + a[k]
    for sec in range(2, k):
        for i in range(1, k - sec + 1):
            j = i + sec
            for x in range(i, j):
                d[i][j] = min(d[i][j], d[i][x] + d[x + 1][j] + (s[j] - s[i - 1]))
    print(d[1][k]) 