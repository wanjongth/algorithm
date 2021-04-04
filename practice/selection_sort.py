# 선택정렬
# 가장 작은 데이터를 앞으로 보내는 과정을 N - 1 번 동안 반복


array = [10, 2, 3, 4, 5, 1, 8, 6, 7]

for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # 스와프

print(array)


# 스와프
# 0 인덱스와 1 인덱스의 원소 교체
array = [3, 5]
array[0], array[1] = array[1], array[0]
print(array)
