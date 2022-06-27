re = int(input())
for i in range(re):
    k = int(input())
    n = int(input())
    s = 0
    
    apart = [[0]*(n + 1) for t in range(k + 1)] 

    for q in range(n+1):
            apart[0][q] = q
  
    for i in range(k):
        for j in range(n):
            apart[i+1][j+1]=apart[i][j+1]+apart[i+1][j]
    print(apart[k][n])

