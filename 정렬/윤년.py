# 1 <= year <= 4000
year = int(input())
# 윤년은 4의 배수 and != 100의 배수 or == 400배수
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print('1')
else:
    print('0') 