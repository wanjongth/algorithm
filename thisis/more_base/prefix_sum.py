# 여러개의 쿼리가 들어왔을 경우([L,R] 구간합을 계산하여 배열 P에 저장
# P[R] - P[L-1]

# 데이터의 개수와 전체 데이터 선언
n = 5
data = [10, 20, 30, 40, 50]

# 접두사 합(Prefix Sum) 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# 구간 합 계산
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])