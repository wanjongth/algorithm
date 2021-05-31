# 투 포인터 알고리즘 : 리스트에 순차적으로 접근해야 할 경우 2개의 점 위치(시작점,끝점)를 기록하면서 처리
# 예 : 특정한 합을 가지는 부분 연속 수열 찾기(양의 정수)
# 시작점 - 반복문을 이용하여 증가, 끝점 - 그것에 따라 증가

n = 5 # 데이터의 개수 N
m = 5 # 찾고자 하는 부분합 M
data = [1, 2, 3, 2, 5] # 전체 수열

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)
