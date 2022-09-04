import heapq
import sys

N = int(input())
heap_list = []
tt = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap_list, num)
        heapq.heappush(tt, num)
    else:
        try:
            print(heapq.heappop(heap_list))
        except IndexError:
            print(0)