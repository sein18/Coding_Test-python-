from collections import deque

N,K=map(int, input().split())

cost=[-1]*100001
def bfs(N):
    if N>=K: return N-K
    temp=deque([(N,0)])
    while temp:
        p,sec=temp.popleft()
        if p==K:
            return sec
        cost[p]=sec
        new=2*p
        if new<=100000 and cost[new]==-1:
            temp.appendleft([new,sec])
        new=p+1
        if new<=100000 and cost[new]==-1:
            temp.append([new,sec+1])
        new=p-1
        if 0<=new and cost[new]==-1:
            temp.append([new,sec+1])

print(bfs(N)) 