import sys
input = sys,sys.stdin.readline

n = int(input())

ar = []
for i in range(N):
    x, y = map(int, input().split())
    ar.append([y, x])
    
sar = sorted(ar)

for y,x in sar:
    print(x,y) 