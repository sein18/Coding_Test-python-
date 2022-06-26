num = int(input())
for i in range(num):
    a,st = input().split()
    for s in st:
        print(s*int(a),end="")
    print()
    