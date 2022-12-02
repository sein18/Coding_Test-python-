from collections import deque
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]


            
test = int(input())
for t in range(test):
    N = int(input())
    row, col = map(int, input().split())
    row2, col2 = map(int, input().split())
    chk = [[0]*N for _ in range(N)]
    
    q = deque()
    q.append((row, col)) 
    while q:
        x, y = q.popleft()
        if x == row2 and y == col2:
            break
        for n in range(8):
            x2 = x + dx[n]
            y2 = y + dy[n]

            if 0<=x2<N and 0<= y2<N and chk[x2][y2] == 0:
                chk[x2][y2] = chk[x][y] +1
                q.append((x2, y2))
    print(chk[row2][col2])       
     