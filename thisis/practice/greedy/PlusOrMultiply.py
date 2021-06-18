# 곱하기 혹은 더하기
# 각 자리가 0~9로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 숫자를 확인하며, 숫자 사이에 'x'혹은 '+' 연산자를 넣어 만들어질 수 있는 가장 큰수를 구하는 프로그램을 작성

# 입력 조건
# 여러 개의 숫자로 이루어진 숫자로 구성된 하나의 문자열 s
# 출력 조건
# 만들어 질 수 있는 가장 큰 수

# # 내 풀이
# string = input()

# answer = int(string[0])  # 초기값 -> S의 첫번째 숫자
# # i, i+1 번째 원소 - zip 사용
# for num1, num2 in zip(string, string[1:]):
#     if int(num1) == 0 or int(num1) == 1:  # 0이나 1일때는 더하기
#         answer += int(num2)
#     else:  # 그 외 곱
#         answer *= int(num2)
# print(answer)

# 답안
data = input()
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 0혹은 1인 경우 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
