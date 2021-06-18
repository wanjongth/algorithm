# 볼링공 고르기
# A,B 두 사람이 볼링 치고있음, 두 사람은 서로 무게가 다른 볼링공을 고르려 함, 무게가 적혀있고 공의 번호는 1번부터 순서대로 부여
# 볼링공은 총 N개, 같은 무게의 공이 여러개 있을 수 있지만, 서로 다른 공으로 간주
# N개의 공의 무개가 각각 주어질 때, 두 사람이 볼링공을 고르는 경우의 수를 구하는 프로그램

# 입력 : 첫째줄에 공의 개수 N, 최대 무게 M, 둘째줄에 각 볼링공의 무게 K

# 출력 : 볼링공을 고르는 경우의 수

# 내 코드
from itertools import combinations

n, m = map(int, input().split())

k = list(map(int, input().split()))

# 가능한 모든 조합
all_case = list(combinations(k, 2))


cnt = 0
# 같은 무게 쌍 카운트
for a, b in all_case:
    if a == b:
        cnt += 1

print(len(all_case) - cnt)

# 답안 코드

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in k:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1):
    n -= array[i]  # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n  # B가 선택하는 경우의 수와 곱하기

print(result)
