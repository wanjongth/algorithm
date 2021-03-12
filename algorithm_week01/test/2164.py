from collections import deque
# N장의 카드, 1번부터 N까지의 카드가 순서대로 놓여있음
# 제일 위에있는 카드 바닥에 버리고 그다음 위에있는 카드 제일 아래로
# 1234 -> 234 -> 342 -> 42 -> 24 -> 4

n = int(input())

array = []
for i in range(n):
    array.append(i+1)

# print(array)  # n까지 카드 만들기
q = deque(array)  # deque 사용


while len(q) > 1:  # q의 길이가 1보다 큰 동안에
    q.popleft()  # 제일 위에있는 카드 버리고
    # print(q)
    temp = q.popleft()  # 그다음 카드 뽑아서
    q.append(temp)  # 제일 아래에 넣음

print(q[0])
