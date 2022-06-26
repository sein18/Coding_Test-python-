word = input()
cnt=[-1]*26
i=0
for x in word:
    if(cnt[ord(x)-97]==-1):
        cnt[ord(x)-97]=i
    i+=1

for a in cnt:
    print(a, end=(" "))