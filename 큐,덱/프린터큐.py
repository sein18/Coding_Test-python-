from collections import deque
T=int(input())
for i in range(T):
    n,m=map(int,input().split())
    q=deque(map(int, input().split()))
    index=[0 for _ in range(n)]
    index[m]=1
    count=0
    while q:
        if q[0]==max(q):
            if index[0]==1:
                break
            else:
                q.popleft()
                index.pop(0)
                count+=1
        else:
            q.append(q.popleft())
            index.append(index.pop(0))
    print(count+1) 