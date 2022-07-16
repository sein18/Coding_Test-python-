import sys
 
arr=[]
num = int(sys.stdin.readline())
for i in range(num):
    arr.append(int(sys.stdin.readline()))

arr.sort()
for i in range(num):
    sys.stdout.write(arr([i]))
