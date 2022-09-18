p = int(input())
s = list(map(int , input().split()))
s.sort()
sum1 = 0
sum2 = 0
for i in s:
    sum1 += i
    sum2 += sum1

print(sum2)