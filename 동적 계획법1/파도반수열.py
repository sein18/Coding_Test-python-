import sys
n = int(sys.stdin.readline())
m = {1:1,2:1,3:1,4:2,5:2}
def findresult(number : int)->int:
    if number in m:
        return m[number]
    m[number] = findresult(number-1) + findresult(number-5)
    return m[number]

for _ in range(n):
    num = int(sys.stdin.readline())
    print(findresult(num))