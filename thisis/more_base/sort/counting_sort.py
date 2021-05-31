# 계수 정렬
# 모두 양의 정수 일 때만 사용 가능,
# 데이터 크기의 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용 가능
# 데이터 개수 N, 데이터 중 최댓값 K -> 시간 복잡도 O(N+K)
# 최댓값의 + 1 만큼 리스트 초기화 -> 너무 큰 범위는 좋지 않다


array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1  # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)):  # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ')  # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
