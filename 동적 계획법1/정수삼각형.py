import sys
input = sys.stdin.readline()

n = int(input())

tri = []
for _ in range(n):
    tri.append(list(map(int,input().split())))

for j in range(2,n+1):
    for i in range(len(tri[-j])):
        tri[-j][i] += max(tri[-j+1][i], tri[-j+1][i+1])

print(tri[0][0])