text = input()
a,b = map(int,text.split())
if b-45>=0:
    print(a,b-45)
elif a==0:
    a=23
    b=b+15
    print(a,b)
else:
    a-=1
    b+=15
    print(a,b)

