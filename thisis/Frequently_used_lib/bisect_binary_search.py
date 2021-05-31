# 이진 탐색 구현을 위한 bisect
# 정렬된 배열에서 특정한 원소를 찾아야 할 때 효과적으로 사용됨
# bisect 라이브러리에서는 bisect_left() 함수와 bisect_right() 함수가 가장 중요하게 사용되고, 시간 복잡도는 O(logN)
# 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할때 인덱스를 찾는 메서드

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

# 값이 특정 범위에 속하는 원소의 개수를 구하고자 할 때 효과적으로 사용됨

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))