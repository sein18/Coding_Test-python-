import sys
N = int(sys.stdin.readline())
wine = [0] * 10000
mxm = [0] * 10000
for n in range(N):
    wine[n] = int(sys.stdin.readline())
mxm[0] = wine[0];
mxm[1] = wine[1]+wine[0]
mxm[2] = max(wine[0]+wine[2],wine[1]+wine[2],mxm[1])
for i in range(3,N):
    mxm[i] = max(wine[i]+wine[i-1]+mxm[i-3],wine[i]+mxm[i-2],mxm[i-1])
print(max(mxm)) 