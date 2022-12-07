import sysN= int(input())
arr = list(map(int, sys.stdin.readline().split()))
result = []
new_arr = sorted(arr)
for x in arr:
    if arr.count(x) == 1:
        place = new_arr.index(x)
        small_list = arr[:place]
        new_set = set(small_list)
        new_list = list(new_set)
        result.append(len(new_list))
    else:
        if x == arr[arr.index(x)]:
            place = new_arr.index(x)
            small_list = new_arr[:place]
            new_set = set(small_list)
            new_list = list(new_set)
            result.append(len(new_list))
        else:
            num = result[arr.index(x)]
            result.append(num)
for x in result:
    print(x, end=' ') 