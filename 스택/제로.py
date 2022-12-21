num = int(input())
li=[]
for i in range(num):
    x = int(input())
    if x == 0:
        li.pop()
    else:
        li.append(x)

print(sum(li))    
