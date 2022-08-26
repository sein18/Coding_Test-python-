from collections import deque
import sys
n=int(sys.stdin.readline())
deq=deque()
for i in range(n):
    com=sys.stdin.readline().split()
    if com[0]=='push_back':
        deq.append(com[1])
    elif com[0]=='push_front':
        deq.appendleft(com[1])
    elif com[0]=='size':
        print(len(deq))
    elif com[0]=='empty':
        if len(deq)==0:
            print(1)
        else:
            print(0)
    else:
        if len(deq)==0:
            print(-1)
        elif com[0]=='pop_front':
            print(deq.popleft())
        elif com[0]=='pop_back':
            print(deq.pop())
        elif com[0]=='front':
            print(deq[0])
        elif com[0]=='back':
            print(deq[-1]) 