 
while True:
    str = input()
    if str == '.':
        break
    li = []
    for j in range(len(str)):
        if str[j] == '(' or str[j] == ')' or str[j] == '[' or str[j] == ']':
            li.append(str[j])
        if len(li)>1:
            if li[len(li)-2] == '(' and li[len(li)-1] == ')'or li[len(li)-2] == '[' and li[len(li)-1] == ']':
                del(li[len(li)-2])
                del(li[len(li)-1]) 
    if(len(li) == 0):
        print('yes')
    else:
        print('no')