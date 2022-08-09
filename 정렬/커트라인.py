def bubble (n):
    for i in range(len(n)-1):
        for j in range(len(n)-1-i):
            if n[j] > n[j+1]:
                temp = n[j]
                n[j] = n[j+1]
                n[j+1] = temp

n = int(input())
num_list = []

for i in range(n):
    num_list.append(int(input()))
    
bubble(num_list)

for num in num_list:
    print(num) 