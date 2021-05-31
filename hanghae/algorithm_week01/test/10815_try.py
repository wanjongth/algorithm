# 숫자카드 개수 N
# 가지고 있는 숫자 카드에 적혀있는 정수, 같은 수가 적혀있는 경우는 없음
# 가지고 있는 숫자 카드인지 아닌지 구해야할 M개의 정수
# M에 대해 가지고 있으면 1, 아니면 0
n = int(input())
n_array = list(map(int, input().split()))
m = int(input())
m_array = list(map(int, input().split()))

n_array.sort()  # 비교하는 곳은 sort 되어 있어야 이분 탐색을 이용하므로

for i in m_array:
    min, max = 0, n
    while min <= max:
        mid = (min + max) // 2
        if 0 <= mid < n:
            if n_array[mid] < i:
                min = mid + 1
            else:
                max = mid - 1
        else:
            break
    if 0 <= max + 1 < n:
        if n_array[max + 1] == i:
            print(1, end=" ")
        else:
            print(0, end=" ")
    else:
        print(0, end=" ")


# # 순차 탐색 : 시간초과
# n = int(input())
# n_array = list(map(int, input().split()))
# m = int(input())
# m_array = list(map(int, input().split()))

# check = list()
# for num in m_array:
#     if num in n_array:
#         check.append(1)
#     else:
#         check.append(0)

# for i in range(len(check)):
#     print(check[i], end=' ')
