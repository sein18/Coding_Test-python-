# def solution(citations):
#     st = []      
#     answer = 0
#     for i in range(len(citations)):
#         cnt = 0
#         for j in citations:
#             if i<=j:
#                 cnt+=1
#         st.append(cnt)
    
#     for i in range(len(st)-1,0,-1):
#         if(st[i]==i):
#             return i

def solution(citations):
    answer = 0
    array = [0]*10001
    for i in citations:
        array[i] += 1

    for i in range(10001):
        if i <= sum(array[i:]):
            answer = i
    return answer

print(solution([3, 0, 6, 1, 5]))





 