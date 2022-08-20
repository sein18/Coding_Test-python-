import sys

N = int(sys.stdin.readline().strip())
a= [[]for N in range(N)]

for i in range(N):
    age, user_name = sys.stdin.readline().split()
    a[i].append(int(age))
    a[i].append(user_name)
    a[i].append(i)

a.sort(key=lambda registerd_order: registerd_order[2])
a.sort(key=lambda registerd_order: registerd_order[0])

for j in a:
    print('{} {}'.format(j[0],j[1])) 