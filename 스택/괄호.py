num = int(input())
for i in range(num):
    str = input()
    li=[]
    for j in range(len(str)):
        li.append(str[j])
        if len(li) > 1:
            if li[len(li)-2] == '(' and li[len(li)-1] == ')':
                del(li[len(li)-2])
                del(li[len(li)-1]) 
    if(len(li) == 0):
        print('YES')
    else:
        print('NO')