# 문자열 재정렬
# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열 입력
# 오름차순으로 정렬하여 이어서 출력, 뒤에 모든 숫자를 더한 값을 이어서 출력

# isalpha, isnumeric 이용
string = input()

answer = []
num = 0
for s in string:
    if s.isalpha():
        answer.append(s)
    elif s.isnumeric():
        num += int(s)
# sort 이용
answer.sort()
# join 이용
answer = ''.join(answer)
answer += str(num)
print(answer)

# 답안
# 생각하지 못한 것, num이 없을 경우 0이 붙게 됨

data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

# 조건 추가
if value != 0:
    result.append(str(value))

print(''.join(result))
