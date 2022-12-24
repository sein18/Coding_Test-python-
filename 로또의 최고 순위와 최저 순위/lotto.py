 
def solution(lottos, win_nums):
    cnt = 0
    cnt1 = 0
    answer = [] 

    for i in lottos:
        for j in win_nums:
            if i == j:
                cnt = cnt + 1
        if i == 0:
            cnt1 = cnt1  + 1

    cnt2 = cnt1 + cnt

    win={6:1,5:2,4:3,3:4,2:5}
    cnt2 = win.get(cnt2,6)
    cnt1 = win.get(cnt1,6)
    answer.append(cnt2)
    answer.append(cnt1)
    return answer

lottos = [44, 1, 0, 0, 31, 25] 
win_nums = [31, 10, 45, 1, 6, 19]

print(solution(lottos,win_nums))