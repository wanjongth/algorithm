# 순차 탐색
# 정말 많이 사용됨 -> 리스트에 특정 값의 원소가 있는지 체크, count()메서드에서도 내부에서 순차 탐색 수행

# 구현
def sequential_search(n, target, array):
    # 각 원소를 확인하면서
    for i in range(n):
        # 현재의 원소가 타겟과 같다면
        if array[i] == target:
            # 현재의 위치를 반환
            return i + 1


print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열 입력")

input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열 입력")
array = input().split()

print(sequential_search(n, target, array))

# 정렬 여부와 상관없이 가장 앞에 있는 원소부터 하나씩 확인함
# 데이터 개수가 N 일 때 최대 N의 비교연산 -> O(N)
