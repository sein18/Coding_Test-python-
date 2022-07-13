def solution(arr):
    answer = []
    for i in range(len(arr)):
        if answer == []:
            answer.append(arr[i])
        elif arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer

print(solution([4,4,4,3,3]))