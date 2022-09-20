import sys
input = sys.stdin.readline

a=input().rstrip()
from collections import deque
nums=deque()
cals=deque()

help=''
for i in range(len(a)):
    if a[i].isnumeric():
        help+=a[i]
    else: #연산자 발견
        nums.append(int(help))
        cals.append(a[i])
        help=''

nums.append(int(help))

#print(nums,cals)

ans=nums.popleft()

ismi=False
for i in range(len(nums)):
    if cals[i]=='-':
        ismi=True

    if ismi==False:
        ans+=nums[i]
    else:
        ans-=nums[i]

print(ans) 
