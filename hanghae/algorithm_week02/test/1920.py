# 수 찾기 - 이분탐색

# N개의 정수가 주어졌을 때 이 안에 X라는 정수가 존재하는지 판단
# 입력 : 첫째 줄 - N, 둘째 줄 - N개의 정수 A[1],A[2]....A[N]
# 그다음 M, A안에 존재하는지.


n = int(input())
A = list(map(int, input().split()))
A.sort()  # 이분탐색을 하려면 정렬 되어야함
m = int(input())
B = list(map(int, input().split()))


def binary_search(target, array):  # 이분탐색
    current_min = 0  # 현재 최소의 인덱스
    current_max = n-1  # 현재 최대의 인덱스
    cursor = (current_min + current_max) // 2  # 현재 커서

    while current_min <= current_max:
        if array[cursor] == target:  # 찾았다면 1을 리턴
            return 1
        elif array[cursor] < target:  # 현재 커서의 값이 타겟보다 작다면
            current_min = cursor + 1  # 최소 인덱스를 커서보다 1 증가
        else:
            current_max = cursor - 1  # 최대 인덱스를 커서보다 1 감소

        cursor = (current_max + current_min)//2  # 커서를 바꿔주고 반복문 돌게함
    return 0  # 위를 충족하지 않으면 0 리턴


for i in range(m):
    print(binary_search(B[i], A))
