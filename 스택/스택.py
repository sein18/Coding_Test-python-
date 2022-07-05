import sys

num =int(sys.stdin.readline())   
que = []
T = -1

def pop():
    global T
    if T == -1:
        print(T)
    else:
        print(que.pop())
        T-=1

def size(): 
    print(len(que))

def empty():
    if T == -1:
        print(1)
    else:
        print(0) 

def top():
    if T == -1:
        print(-1)
    else:
        print(que[T])



def push(x): 
    global T
    que.append(x)
    T+=1

for i in range(num):
    order = sys.stdin.readline().rstrip()
    print(order)
    if order == 'pop':
        pop()
    elif order == 'size':
        size()
    elif order == 'empty':
        empty()
    elif order == 'top':
        top()
    else:
        order, x = map(str,order.split())
        push(x) 

