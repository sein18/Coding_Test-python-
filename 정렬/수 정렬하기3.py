import sys
 
arr=[0]*10000
num = int(sys.stdin.readline())
for i in range(num):
    inum=(int(sys.stdin.readline()))
    arr[inum-1]+=1

for i in range(10000):
    if arr[i]!=0:
        for j in range(arr[i]):
            print(i+1)
 