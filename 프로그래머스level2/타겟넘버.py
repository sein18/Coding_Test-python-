from operator import le


def solution(numbers, target):
    answer = 0
    leavers=[0]
    for num in numbers:
        tmp=[]
        for parent in leavers:
            tmp.append(parent+num)
            tmp.append(parent-num)
        leavers=tmp
    for num in leavers:
        if num == target:
            answer+=1
    return answer

print(solution([1, 1, 1, 1, 1],3))