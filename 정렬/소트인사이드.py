num = int(input())

numlist = list(str(num))

numlist.sort(reverse=True)

lt = "".join(numlist)

print(lt)