import heapq
from inspect import stack
import sys
input = sys.stdin.readline
n = int(input())
#중간값 보다 큰 값은 오른쪽 힙, 작은 값은 왼쪽 힙에 넣는다.
left_h, right_h = [], []
for i in range(n):
    x = int(input())
    if len(left_h) == len(right_h):
        heapq.heappush(left_h, -x)
    else:
        heapq.heappush(right_h, x)
    #만약 오른쪽 힙이 왼쪽 힙보다 작아지면 자리 교환
    if right_h and right_h[0] < -left_h[0]:
        lv = heapq.heappop(left_h)
        rv = heapq.heappop(right_h)
        heapq.heappush(left_h, -rv)
        heapq.heappush(right_h, -lv)
    print(-left_h[0]) 