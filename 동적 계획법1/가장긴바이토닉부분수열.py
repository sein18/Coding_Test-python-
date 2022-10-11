import sys
read = sys.stdin.readline

N = int(read())
A = list(map(int, read().split()))
forward = [0] * N
backward = [0] * N

def calc(reverse=False):
    if reverse:
        temp = [A[-1]]
        seq = backward
        r = range(N-1, -1, -1)
    else:
        temp = [A[0]]
        seq = forward
        r = range(N)

    for i in r:
        if temp[-1] < A[i]:
            temp.append(A[i])
        else:
            idx = 0
            for j in range(len(temp)):
                if temp[j] < A[i]:
                    idx += 1
                else:
                    temp[idx] = A[i]
                    break
        seq[i] = len(temp)

calc()
calc(True)

res = -1
for i in range(N):
    res = max(res, forward[i] + backward[i])