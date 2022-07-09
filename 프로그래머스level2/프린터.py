def solution(priorities, location):
    
    ind = [ [priorities[x], x] for x in range(len(priorities))]
    num = ind[location]
    max = ind[0]
    print(max)    
print(solution([1, 1, 9, 1, 1, 1],0))
