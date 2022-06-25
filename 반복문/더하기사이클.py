x=int(input())
y=x
num=1
for i in range(9999):
    a=y//10 
    b=y%10 
    c=a+b 
    y=(y%10)*10+c%10 
    if(y != x):
        num+=1
    else:
        break
print(num)