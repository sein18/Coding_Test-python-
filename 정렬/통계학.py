import sys
from collections import Counter

tc = int(sys.stdin.readline())
arr = [] # 테스트 숫자 입력 받는 배열
for i in range(0, tc):
    arr.append(int(sys.stdin.readline()))

arr.sort()
avg = round(sum(arr)/tc)
center = int(arr[int((tc-1)/2)])
mode = Counter(arr)
freq = mode.most_common()
if len(arr) > 1 and freq[0][1] == freq[1][1]:
    ans = freq[1][0]
else:
    ans = freq[0][0]

ran = arr[tc-1] - arr[0]

print(avg)
print(center)
print(ans)
print(ran) 