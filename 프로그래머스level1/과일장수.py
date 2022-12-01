def solution(k,m,score):
    answer = 0
    score.sort(reverse=True)
    box_num = len(score)
    for i in range(box_num):
        p = score[i*m+m-1]
        answer+=p*m
    return answer