import sys
input = sys.stdin.readline

n=int(input())
l=[]
for i in range(n):
    r,g,b=map(int,input().rstrip().split())
    l.append([r,g,b])

suml=[]

def dfs(idx):
    if idx==n-2:
        #print(s)
        sum=0
        for i in range(n):
            sum+=l[i][s[i]]
        suml.append(sum)
        return

    for i in range(1): #0 1 2
        if s[-1]==0:
            s.append(1)
            dfs(idx+1)
            s.pop()

            s.append(2)
            dfs(idx+1)
            s.pop()
      
        elif s[-1]==1:
            s.append(0)
            dfs(idx+1)
            s.pop()

            s.append(2)
            dfs(idx+1)
            s.pop()

        elif s[-1]==2:
            s.append(0)
            dfs(idx+1)
            s.pop()

            s.append(1)
            dfs(idx+1)
            s.pop()

for i in range(n):
    s=[i]
    dfs(-1)

print(min(suml))