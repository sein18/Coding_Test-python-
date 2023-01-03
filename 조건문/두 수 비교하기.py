text = input()
a,b = map(int,text.split())
if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')