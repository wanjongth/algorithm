# 못품

import sys
import collections

N, M = map(int, sys.stdin.readline().split())
M_array = list(map(int, sys.stdin.readline().split()))

# print(N, M)
# print(M_array)
# 1부터 N까지 배열 만들기
N_array = list(range(1, N+1))
count = 0
# print(N_array)

for i in range(M):
    N_len = len(N_array)
    N_index = N_array.index(M_array[i])

    if N_index > N_len - N_index:  # left
        while True:
            if i == N_array[0]:
                N_array.pop(0)
                break
            else:
                count += 1
                left = N_array.pop(0)  # 첫번째꺼 끄집어내기
                N_array.append(left)  # 끄집어낸거 리스트에 담기
                # print(count)
    else:
        while True:
            if i == N_array[0]:
                N_array.pop(0)
                break
            else:
                count += 1
                right = N_array.pop(-1)  # 끝 끄집어내기
                deq = collections.deque(N_array)  # 왼쪽에 넣기 위해  덱으로 변환
                deq.appendleft(right)
                N_array = list(deq)
                # print(count)

print(count)
