import sys
a = int(sys.stdin.readline().rstrip())
for i in range(a):
    x,y = map(int,sys.stdin.readline().split())
    print(x+y)