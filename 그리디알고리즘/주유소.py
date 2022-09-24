#
# * 백준 13305: 주유소
#
# Greedy algorithm 을 이용
# 기름값이 올라가는 구간에는 기름을 넣지 않는다
#

from sys import stdin

# 2 <= n <= 100,000
n = int(stdin.readline())

# 1 <= edge <= 1,000,000,000, n - 1 개
edge = list(map(int, stdin.readline().split()))

# 1 <= price <= 1,000,000,000, n 개
price = list(map(int, stdin.readline().split()))

answer = 0
cost = price[0]
for i in range(n - 1):
    if cost > price[i]:
        cost = price[i]
    answer += cost * edge[i]

print(answer)

