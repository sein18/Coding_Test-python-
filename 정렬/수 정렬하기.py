 

arr=[]
num = int(input())
for i in range(num):
    arr.append(int(input()))

arr.sort()
for i in range(num):
    print(arr[i])
