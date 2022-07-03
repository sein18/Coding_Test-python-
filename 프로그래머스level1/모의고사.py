def solution(answers):
    answer = []
    a=[1,2,3,4,5]*5000
    b=[2,1,2,3,2,4,2,5]*1500
    c=[3,3,1,1,2,2,4,4,5,5]*1000

    numname = [1,2,3]
    num = [0,0,0]
    
    for i in range(len(answers)):
        if a[i] == answers[i]:
            num[0]+=1
        if b[i] == answers[i]:
            num[1]+=1
        if c[i] == answers[i]:
            num[2]+=1
     
    for i in range(3):
        if max(num) == num[i]:
            answer.append(numname[i])
    return answer

answers=[1,3,2,4,2]

print(solution(answers))