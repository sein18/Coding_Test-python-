def solution(board, moves):
    x=[]
    answer=0
    for i in moves: #1,5,3,5,1,2,1,4
        for j in range(len(board[0])): # 0,1,2,3,4
            if board[j][i-1] == 0:
                continue
            else:
                x.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if len(x) > 1:
            if x[len(x)-1] == x[len(x)-2]:
                x.pop()
                x.pop()
                answer += 2

    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))