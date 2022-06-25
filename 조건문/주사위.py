text = input()
a,b,c = map(int,text.split()) 
x=[a,b,c]
x.sort(reverse=True)
if x[0]==x[1]==x[2]:
    print(x[0]*1000+10000)
elif x[0]==x[1]:
    print(1000+x[0]*100)
elif x[1]==x[2]:
    print(1000+x[1]*100)
else:
    print(x[0]*100)
