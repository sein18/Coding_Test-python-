def solution(N, stages):
    answer = [] 
    num = [] 
    t = []
    for i in range(1,N+1):
        answer.append(i) 

    for i in range(N):
        n = 0
        k = 0
        for j in range(len(stages)):
            if stages[j] >= answer[i]:
                n += 1
            if stages[j] == answer[i]:
                k += 1 
        num.append(k/n)     
        t.append([num[i], answer[i]])
    
    t.sort(key = lambda x:x[0], reverse=True)
    x = []
    for i in t:
        x.append(i[1])
    return x

print(solution(4,[4,4,4,4,4]))


# from collections import Counter
 
 
# def solution(N, stages):  # N: 스테이지의 개수, stages: 현재 도전 중인 스테이지 번호
#     answer = []
 
#     stages_clear = []  # 스테이지를 클리어한 사람 수
 
#     count = Counter(stages)
#     total = len(stages)
 
#     for i in range(1, N + 1):
#         total -= count[i]
#         stages_clear.append(total)
#         if count[i] == 0:
#             answer.append((i, 0))
#         else:
#             answer.append((i, count[i] / (total + count[i])))
 
#     answer = [idx for idx, v in sorted(answer, key=lambda x: -x[1])]
 
#     return answer