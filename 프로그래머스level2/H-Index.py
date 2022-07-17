def solution(citations):
    st = []      
    answer = 0
    citations = sorted(citations,reverse=True) 
    for i in range(len(citations)):
        cnt = 0
        for j in citations:
            if i<=j:
                cnt+=1
        st.append(cnt)
    
    for i in range(len(st)-1,0,-1):
        if(st[i]==i):
            return i

print(solution([3, 0, 6, 1, 5]))

# def solution(citations):
      
#     answer = 0
#     for i in range(max(citations),0,-1):
#         cnt = 0
#         for j in citations:
#             if i<=j:
#                 cnt+=1
#             if cnt == i:
#                 return cnt
         
# print(solution([3, 0, 6, 1, 5]))