n,m = map(int,input().split())
pull_list = list(map(int,input().split()))
num_list = list(range(1,n+1))

def pull(list):
    list.pop(0)

def l_Shift(list):
    list.append(list.pop(0))

def r_Shift(list):
    list.insert(0,list.pop())

count=0
pull_num=0
while len(pull_list)>0 :
    pull_num = pull_list.pop(0)
    if num_list.index(pull_num) <= len(num_list)-1-num_list.index(pull_num):
        while num_list[0] != pull_num:
            l_Shift(num_list)
            count += 1
        pull(num_list)
    elif num_list.index(pull_num) > len(num_list)-1-num_list.index(pull_num):
        while num_list[0] != pull_num:
            r_Shift(num_list)
            count += 1
        pull(num_list)
    else :
        pull(num_list)
print(count) 