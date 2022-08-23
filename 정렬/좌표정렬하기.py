N = int(input())
ar = []
for i in range(N):
    x, y = map(int, input().split())
    ar.append([x, y])
    
ar.sort()

for i in range(N):
    print(ar[i][0], ar[i][1]) 