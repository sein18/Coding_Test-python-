import sys
N = int(sys.stdin.readline())

M=[]
for i in range(N):
    M.append(sys.stdin.readline().rstrip())
M= list(set(M))
M.sort(key=lambda x: (len(x),x))
for i in M:
    print(i)
