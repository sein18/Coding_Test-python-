def solution(people, limit):
    answer = 0
    
    people.sort()
   
    sum=0
    num=0 
    idx=0
    while len(people)!=1:
        sum += people[idx]
        if sum > limit:
            answer+=1
            for i in range(idx): 
                people.pop(0)
            sum=0
            idx=-1
        idx+=1
    return answer+1

print(solution([70, 80, 50],100))