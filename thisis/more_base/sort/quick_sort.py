# 퀵 정렬
# 많이 사용되는 정렬 알고리즘
# 대부분의 프로그래밍 언어에서 정렬 라이브러리의 근간이 되는 알고리즘

# 접근 방식 : 기준 데이터를 설정하여 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다.
# 피벗(pivot)사용 - 큰 숫자와 작은 숫자를 교환할 때 교환하기 위한 기준
# 호어 분할 방식(대표적) -> 리스트에서 첫 번째 데이터를 피벗으로 정한다.

# array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


# def quick_sort(array, start, end):
#     if start >= end:
#         return
#     pivot = start
#     left = start + 1
#     right = end
#     while left <= right:
#         # 피벗보다 큰 데이터를 찾을 때까지
#         while left <= end and array[left] <= array[pivot]:
#             left += 1
#         # 피벗보다 작은 데이터를 찾을 때까지
#         while right > start and array[right] >= array[pivot]:
#             right -= 1
#         if left > right:  # 엇갈렸다면 작은 데이터와 피벗을 교체
#             array[right], array[pivot] = array[pivot], array[right]
#         else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
#             array[left], array[right] = array[right], array[left]

#         # 분할 이후에 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
#         quick_sort(array, start, right - 1)
#         quick_sort(array, right + 1, end)


# quick_sort(array, 0, len(array) - 1)
# print(array)

# 파이썬 버전
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))
