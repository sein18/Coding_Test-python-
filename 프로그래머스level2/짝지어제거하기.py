def solution(s):
    answer = -1

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
 
    x=[]
    for i in s:
        x.append(i)
        if len(x) >= 2 and x[len(x)-2] == x[len(x)-1]:
            x.pop()
            x.pop() 
        print(x)
    if x==[]:
        answer=1
    else:
        answer=0
    return answer


print(solution("baabaa"))