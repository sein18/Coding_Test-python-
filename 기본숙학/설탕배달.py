x = int(input())
num=0
while x>=0:
    if x%5==0:
        num+=(x//5)
        print(num)
        break
    x-=3
    num+=1
else:
    print(-1)
         