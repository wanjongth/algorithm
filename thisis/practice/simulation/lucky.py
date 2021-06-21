# 럭키 스트레이트
# 게임 내에서 점수가 특정 조건을 만족할 때만 사용할 수 있는 럭키 스트레이트
# 현재 캐릭터의 점수를 N이라고 할 때 자릿수를 기준으로 점수 N을 반으로 나누어
# 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황을 의미
# 현재 점수 N이 주어지면 럭키 스트레이트를 사요할 수 있는 상태인지 아닌지 알려주는 프로그램

# 입력 - N, 자릿수는 항상 짝수
# 출력 - 있으면 lucky, 없으면 Ready 출력

# 슬라이싱 이용
n = int(input())
n = str(n)
half = int(len(n)/2)

left = n[half:]
right = n[:half]

left_arr = []
right_arr = []
for i in range(half):
    left_arr.append(int(left[i]))
    right_arr.append(int(right[i]))

if sum(left_arr) == sum(right_arr):
    print('LUCKY')
else:
    print('READY')

# 답안
# summary 라는 변수를 이용하여 비교, for문의 범위를 조정하여 답안 도출

n = input()
length = len(n)
summary = 0

for i in range(length//2):
    summary += int(n[i])

for i in range(length // 2, length):
    summary -= int(n[i])

if summary == 0:
    print("LUCKY")
else:
    print("READY")
