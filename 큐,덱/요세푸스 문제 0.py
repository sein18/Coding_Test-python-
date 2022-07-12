a,b = map(int,input().split())
c=[]
for i in range(1,a+1):
    c.append(i)     

x=[]
b=b-1
num=b
while True:
    if c==[]:
        break
    if(num<len(c)):
        x.append(c[num])
        del(c[num]) 
        num += b
    else: 
        num=num%len(c)
        x.append(c[num])
        del(c[num])
        num += b

print('<', end='')
for i in x:
    if i == x[a-1]:
        print(i,end=">")
    else:
        print(i,end=", ")
 