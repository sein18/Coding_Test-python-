from collections import deque
import sys
input = sys.stdin.readline

k = int(input())
color = [0,2,1]

def bfs(v) :
    q = deque()
    q.append(v)
    visited[v] = 1

    while q :
        n = q.popleft()

        for i in graph[n] :
            if visited[i] == 0:
                q.append(i)
                visited[i] = color[visited[n]]

            elif visited[n] == visited[i] : # 방문한 노드의 색과 인접한 노드의 색이 같을 때
                return False
    return True

for _ in range(0, k) :
    v, e = map(int, input().split(' '))
    graph = [[] for _ in range(0, v + 1)]
    visited = [0] * (v + 1)

    for _ in range(0, e) :
        x, y = map(int, input().split(' '))
        graph[x].append(y)
        graph[y].append(x)

    result = True

   # ﻿모든 정점이 연결된 그래프가 아닐 수도 있기 때문에 방문 안 된 정점들에 대해 bfs 진행
    for i in range(1, v+1) :
        if visited[i] == 0 :
            result = bfs(i)
            if not result :
                break

    print("YES" if result else "NO") 