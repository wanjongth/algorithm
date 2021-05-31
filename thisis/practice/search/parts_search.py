# 부품 찾기

# 부품이 N개, M개 종류의 부품
# M개 종류가 모두 있는지 확인하는 프로그램

# 입력
# 첫째 줄:N, 둘째 줄: 공백 구분하여 N개의 정수, 셋째 줄:M, 넷째 줄: 공백 구분하여 M개의 정수
# 출력
# 각 부품이 있으면 yes 없으면 no (공백 구분)
# 입력 예
# 5
# 8 3 7 9 2
# 3
# 5 7 9

# 이진 탐색 풀이
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None  # 없을 경우 None


n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
target_array = list(map(int, input().split()))

for i in target_array:
    if binary_search(array, i, 0, n-1) == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")

# 계수 정렬 풀이
n = int(input())
array = [0] * 1000001

for i in input().split():  # 이렇게 받아서 쓸 수도 있구나
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 집합 풀이
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
