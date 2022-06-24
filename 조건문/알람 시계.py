text = input()
 
a,b,c = map(int,text.split()) 

if b+x>=60:
    a+=(b + x)//60
    if a>=24:
        a-=24
    b=(b + x) % 60
    print(a,b)
else:
    print(a,b + x)

