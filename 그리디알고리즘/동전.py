N, change = map(int, input().split())
coin_list = []

for n in range(N):
    coin_list.append(int(input()))
    
count = 0

for coin in coin_list[::-1]:
    if coin == 0: break
    count += change // coin
    change %= coin
    
print(count) 