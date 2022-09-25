import sys
# '<-' means '='
def fib(n):
    if n == 1 or n == 2:
        return 1 # Code 1
    else:
        value = fib(n-1) + fib(n-2)
        return value

def fibonacci(n):
    f = [0]*(n+1)
    f[1], f[2] = 1, 1
    count = 0
    for i in range(3,n+1):
        count += 1
        f[i] = f[i-1] + f[i-2] # Code 2
    return count
n = int(sys.stdin.readline().rstrip())
print(fib(n),fibonacci(n)) 
