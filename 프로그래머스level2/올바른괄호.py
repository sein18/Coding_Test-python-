def solution(s):
    answer = True
    x=[]
    for i in s:
        x.append(i)
        if len(x) >= 2 and x[len(x)-2]=='(' and x[len(x)-1]==')':
            x.pop()
            x.pop()
    if len(x)==0:
        return True 
    else:
        return False
print(solution("()()"))