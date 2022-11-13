import sys
sys.setrecursionlimit(10**6)

def bfs(x, y:int):
    a1 = [-1, +1, 0, 0]
    b1 = [0, 0, -1, +1]
    for c in range(4):
        nx, ny = x+a1[c], y+b1[c]
        if (0 <= nx <= N-1) and (0 <= ny <= M-1):
            if map_list[nx][ny] == 1:
                map_list[nx][ny] = 0
                bfs(nx, ny)

T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())
    map_list = [[0]*M for _ in range(N)]
    cnt = 0
    
    for j in range(K):
        y, x = map(int, input().split())
        map_list[x][y] = 1
        
    for a in range(N):
        for b in range(M):
            if map_list[a][b] == 1:
                bfs(a,b)
                cnt += 1
            else:
                continue
    print(cnt)