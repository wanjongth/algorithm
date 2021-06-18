# 모험가 길드
# N명의 모험가를 대상으로 공포도를 측정했는데, 공포도가 높은 모험가는 위험 상황에서 제대로 대처를 못함.
# 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는 반드시 X명 이상으로 구성

# 입력
# 첫째줄 - N
# 둘째줄 - 각 모험가의 공포도의 값을 N 이하의 자연수로 주어짐
# 출력
# 여행을 떠날 수 있는 그룹 수의 최댓 값

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

result = 0  # 최종 그룹 수
cnt = 0  # 그룹에 포함된 인원수
for i in arr:
    cnt += 1
    if i <= cnt:
        cnt = 0
        result += 1

print(result)
