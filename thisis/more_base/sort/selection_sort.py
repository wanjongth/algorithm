# 선택 정렬
# 가장 작은 데이터를 앞으로 보내는 과정을 N-1번 반복

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i  # 가장 작은 데이터 담을 그릇
    for j in range(i + 1, len(array)):  # N-1 번 만큼
        if array[min_index] > array[j]:
            min_index = j  # j가 작다면 min_index이다
    array[i], array[min_index] = array[min_index], array[i]  # 스와프 해주고

print(array)  # 출력

# O(N^2)의 시간 복잡도를 보이는 것으로 보아 매우 비효율적이지만,
# 특정한 리스트에서 가장 작은 데이터를 찾는 일이 잦으므로 소스코드 형태에 익숙해질 필요가 있다!
