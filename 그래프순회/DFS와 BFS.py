import sys
from collections import deque

N,M,V = map(int, sys.stdin.readline().split())
a_list = [[False]*(N+1)for i in range(N+1)] 
visited = [False]*(N+1)


for i in range(M):
    a, b =  map(int,sys.stdin.readline().split())
    a_list[a][b] = a_list[b][a] = True

print(visited)
print(a_list)
def dfs(x):
  if visited[x]==False:
    visited[x]=True
    print(x, end=" ")
    for i in range(1,N+1):
      if a_list[x][i]==True:
        dfs(i)

def bfs(x):
  queue = deque([x])
  visited[x]=False
  while queue:
    x=queue.popleft()
    print(x, end=" ")
    for i in range(1, N+1):
      if (visited[i]==True and a_list[x][i]==True):
        visited[i]=False
        queue.append(i)

dfs(V)
print()
bfs(V)