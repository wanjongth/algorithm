# 소스코드를 작성할 때 문자열 안에 큰따옴표나 작은따옴표가 포함되는 경우.
data = 'Hello World'
print(data)

data = "Don't you know \"Python\"?"
print(data)

# 문자열 연산
a = "Hello"
b = "World"

print(a + " " + b)

# 문자열 변수를 양의 정수와 곱하는 경우
print(a * 3)

# 파이썬의 문자열은 내부적으로 리스트와 같이 처리됨 = 여러 개의 문자가 합쳐진 리스트(인덱싱 / 슬라이싱 가능)
a = "ABCDEF"
print(a[2 :4])