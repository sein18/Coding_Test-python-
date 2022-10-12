import sys
input = sys.stdin.readline

#전기줄개수n 100개, 총 번호 500, 500까지
n=int(input())
dp=[1]*n
l=[]
for i in range(n):
    a,b=map(int,input().split())
    l.append([a,b])

l=sorted(l)


for i in range(1,n): #i=1~ n-1
    for j in range(0,i): #j=0~ i-1
        if l[i][0]>l[j][0] and l[i][1]>l[j][1]: #이을 수 있는 애들만 검사 
            dp[i]=max(dp[i],dp[j]+1) #LIS. 최대로 잇기
#print(dp)

print(n-max(dp)) #최대로 이어지는 max값만큼 남는 것이니, n-max(dp)가 삭제해야할 최소 수
 
