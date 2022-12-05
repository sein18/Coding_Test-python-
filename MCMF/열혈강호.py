import sys

inp = sys.stdin.readline

def dfs(x):
    for i in g[x]:
        if (ch[i] == 1): continue
        ch[i] = 1
        k = dfs(pos[i])
        if (pos[i] == 0 or k == 1): pos[i] = x; return 1
    return 0

n, m = map(int, inp().split())
pos = [0] * (m + 1)
g = [[] for _ in range(n + 1)]
ans = 0

for i in range(1, n + 1):
    a = [*map(int, inp().split())]
    c = a[0]
    for j in range(1, c + 1):
        g[i].append(a[j])

for i in range(1, n + 1):
    ch = [0] * (m + 1)
    if (dfs(i) == 1): ans += 1

print(ans)