import sys
from bisect import bisect_left, bisect_right

N = int(sys.stdin.readline())
card = sorted(int, sys.stdin.readline().split())

M = int(sys.stdin.readline())
M_list = sorted(int, sys.stdin.readline().split())
result =""
for i in range(N):
    if i ==M-1:
        result += str(bisect_right(card,M_list[i])-bisect_left(card,M_list[i]))
    else:
        result += str(bisect_right(card,M_list[i])-bisect_left(card,M_list[i])) + " "
print(result)