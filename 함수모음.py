# max, min
x= [9.96,1.27,5.07,8.38]
print(max(x),min(x))

# 문자열
txt = 'abcdefghigk'
print(txt[5:8])

# 문자열 홀수
print(txt[::2])

# 거꾸로 츨력
print(txt[8:5:-1])

# 문자열에 특정 문자열 확인
if 'abc' in txt:
    print("text")

# 문자열 길이 len
print(len(txt))

# 문자열 알바벳검사 isalpha()
print(txt.isalpha())

# 문자열 숫자확인 isdigit()
print(txt.isdigit())

# 문자열이 알파벳또는 숫자인지 검사 isalnum()
print(txt.isalnum())

# 문자열 대소문자 변환 (upper.lower)
print(txt.upper(),txt.lower())

# 문자열 좌우 공백제거 (lstrip,rstrip,strip)
print(txt.lstrip(),txt.rstrip(),txt.strip())

# 문자열에 있는 문자(열)개수 구하기(count)
print(txt.count('a'))

# 문자열에서 특정 문자(열)위치 찾기(find)
print(txt.find('igk'))

# 문자열을 특정문자(열)로 분리 (split)
url = 'a/cd/fe/ddd/wwq/aa/dd'
rel = url.split('/')
print(rel)

# 문자열을 특정 문자(열)로 결합하기(join)
rel1 = ':'
print(rel1.join(rel))
# 문자열에서 특정 문자(열)를 다른 문자(열)로 바꾸기 (replace)
print(txt.replace('abc','qqq'))
# 문자열을 정렬 (sorted,join)
print(''.join(sorted(txt,reverse=True)))

# -------------------------------------문자열----------------------------------
# 순차적인 정수 리스트 만들기
re=list(range(1,10,2))
print(re)
# 리스트에서 특정 요소의 위치 구하기
print(re.index(7))
# 리스트 순서를 역순으로 만들기
print(re.reverse()) # 원본이 자체적으로 바뀜
print(re)
# 리스트 순서를 역순으로 만들기(2)
re1 = reversed(re)
print(list(re1))
# 리스트 요소추가(append),특정위치 삽입(insert)
re.append(10)
re.insert(8,11) #인덱스가 넘어버리면 마지막 인덱스에 추가
print(re)
# 리스트 특정 위치 요소제거
del(re[0])
del(re[0:2])
print(re)
# 리스트에서 특정 요소제거
re.remove(3)
print(re)
# 리스트 요소 정렬
re.sort()
re = sorted(re,reverse=True)
print(re)
