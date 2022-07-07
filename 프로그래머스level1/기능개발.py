def solution(progresses, speeds):
    answer = []
    num = 0
    while len(progresses) != 0:
        for i in range(len(progresses)):
            progresses[i]+=speeds[i]
        if(progresses[0]>=100):
            for i in range(len(progresses)):
                j=i
                if(progresses[j-num]>=100): 
                    del(progresses[j-num])
                    del(speeds[j-num])
                    num+=1 
            if num > 0:
                answer.append(num)
                num = 0 
   
    return answer

print(solution([93, 30, 55],[1, 30, 5]))
