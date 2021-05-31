# 컴퓨터 시스템은 대체로 실수 정보를 표현하는 정확도에 한계를 가짐
a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

#이럴 땐 round() 함수 사용

print(round(a, 4))

if round(a, 4) == 0.9:
    print(True)
else:
    print(False)

a = 7
b = 3

# 나누기 - 기본적으로 실수로 표현됨
print(a / b)

# 나머지
print(a % b)

# 몫
print(a // b)

# 제곱
print(a ** b)