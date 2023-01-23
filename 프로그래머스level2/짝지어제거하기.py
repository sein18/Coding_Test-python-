def solution(s):
    answer = -1
 
    x = []
    for i in s:
        x.append(i)
        if len(x) >= 2 and x[len(x)-2] == x[len(x)-1]:
            x.pop()
            x.pop()  
    if x == []:
        answer = 1
    else:
        answer = 0
    return answer


print(solution("baabaa"))