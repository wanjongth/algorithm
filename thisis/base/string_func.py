# count
a = "hobby"
print(a.count('b'))

# 처음 나온 위치 알려주기 - find
# 찾는 문자가 없으면 -1 출력
print(a.find('b'))
# index = 처음 나온 위치 알려주기.
# find와 다른점은 찾는 문자가 없으면 에러 발생

# join - 문자열 삽입. 문자열의 문자 사이에 해당 문자를 삽입 - 리스트와 튜플에도 사용 가능
print(",".join('abcd'))

# upper, lower - 대, 소문자 변환
print(a.upper())

# strip - 공백 지우기, lstrip, rstrip
a = " hi "
print(a.strip())
print(a.lstrip())
print(a.rstrip())

# replace - 문자열 바꾸기
a = "Life is too short"
print(a.replace("Life", "Your leg"))

# split - 문자열 나누기
# 입력받을때 많이 사용하는데 매개변수가 없으면 공백, 특정 값이 있을 경우 구분자로 사용
b = "a:b:c:d"
print(b.split(':'))
