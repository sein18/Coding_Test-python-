X = int(input())
count = 0

while X != 1:
    count += 1
    if X%3 == 0:
        X /= 3
    elif X%2 == 0:
        X /= 2
    else:
        X -= 1
print(int(count))