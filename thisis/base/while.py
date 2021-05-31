# 특정한 소스코드를 반복적으로 실행하고자 할 때,
# for 와 while 중 어떤 것을 사용해도 상관 없으나, 코테에서 실제 사용 예시를 확인해 보면 대부분의 경우에서 for문이 소스코드가 짧은경우가 많다.

# while - 조건문이 참일 때 한해서, 반복적으로 코드 수행
i = 1
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    result += i
    i += 1
print(result)

i = 1
result = 0
while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1
print(result)