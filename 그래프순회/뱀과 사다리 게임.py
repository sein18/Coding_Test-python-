from collections import deque
N, M = map(int, input().split())
board = list(range(0, 101))
visit = [float("inf")] * 101
visit[1] = 0
for i in range(N + M):
    x, y = map(int, input().split())
    board[x] = y

q = deque([(1, 0)])
while q:
    here, hereC = q.popleft()
    for i in range(1, 7):
        there = here + i
        if there > 100:
            break
        if visit[there] > hereC + 1:
            q.append([board[there], hereC + 1])
            visit[there] = hereC + 1
print(visit[-1])