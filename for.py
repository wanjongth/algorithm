# for 변수 in 리스트:
#     실행할 소스코드
# in 뒤의 데이터로는 리스트, 튜플, 문자열 등이 사용될 수 있다.

result = 0

# i는 1부터 9까지의 모든 값을 순회
# range() - range(시작 값, 끝 값 + 1) 형태
for i  in range(1, 10):
    result += i
print(result)

# range()의 값으로 하나의 값만을 넣으면, 자동으로 시작 값은 0 - 주로 리스트나 튜플 데이터의 모든 원소를 첫 번째 인덱스부터 방문해야 할 때 이 방법 사용
scores = [90, 85, 77, 65, 97]

for i in range(5):
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")

# 반복문 안에서 continue를 만나면 프로그램의 흐름은 반복문의 처음으로 돌아간다.
# 위의 예제에서 2번과 4번은 블랙리스트에 올라가 있어 점수가 높아도 합격하지 못한다고 가정해보면
# 블랙리스트에 해당 번호가 포함된 경우, 해당 학생은 무시화고 다시 다음 번호부터 처리하도록 돌아가게 함

scores = [90, 85, 77, 65, 97]
cheating_list = {2, 4}

for i in range(5):
    if i + 1 in cheating_list:
        continue
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")

# 반복문의 중첩
# 대표적인 예시의 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i, "X", j, i * j)
    print()
