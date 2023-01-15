import sys
input=sys.stdin.readline

num = [0]*21
for _ in range(int(input())):
    line = input().split()
    cmd = line[0]
    if cmd == "all":
        num = [1]*21
    elif cmd == "empty":
        num = [0]*21
    else:
        n = int(line[1])
        if cmd == "add": 
            num[n] = 1
        elif cmd == "remove":
            num[n] = 0
        elif cmd == "check":
            if num[n]: print(1)
            else: print(0)
        else:
            if num[n]: num[n] = 0
            else: num[n] = 1 