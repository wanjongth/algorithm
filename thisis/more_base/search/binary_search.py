# 이진 탐색
# 정렬 되어 있을 때 사용할 수 있는 탐색 알고리즘
# 시작점, 끝점, 중간점을 이용하여 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교

# # 구현
# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     # 찾은 경우 중간점 인덱스 반환
#     if target == array[mid]:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid-1)
#     else:
#         return binary_search(array, target, mid + 1, end)


# n, target = list(map(int, input().split()))
# array = list(map(int, input().split()))

# result = binary_search(array, target, 0, n - 1)
# if result == None:
#     print("원소가 존재하지 않습니다.")
# else:
#     print(result + 1)

# 반복문으로 구현
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


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

# 처음부터 구현을 제대로 하기 힘드나 코드를 암기하고 있으면 좋다
# 코테에서 범위가 2,000만을 넘어가면 이진 탐색으로 접근(시간복잡도 : O(logN))
# 이진 탐색 문제는 입력 데이터가 많거나, 탐색 범위가 매우 넓은 편인데,
# 이럴 때 input()을 사용하면 시간초과가 빈번히 발생
# sys.stdin.readline() 사용하자 -> .rstrip() 꼭 호출하자 -> 엔터가 개행문자로 들어올 수 있기 때문에 공백을 없애야 한다
