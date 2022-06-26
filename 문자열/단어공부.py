s = input()
s = s.lower()
cnt=[0]*26
num=0
for x in s:
    cnt[(ord(x)-97)]+=1

for i in range(len(cnt)): 
    if(max(cnt)==cnt[i]):
        num+=1
if(num>1):
    print("?")
else:
    for i in range(len(cnt)): 
        if(max(cnt)==cnt[i]):
            print(chr(i+97).upper())    
