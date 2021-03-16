# 제로 - 스택

# 돈 관리하는데 잘못된 수를 부르면 0을 외쳐 가장 최근(스택) 쓴 수를 지우게 함
# 모든 수를 받아 적은 후 그 수의 합

# 입력: 첫째줄 - K 이후 - K개의 줄에 정수 1개씩
# 0일 경우는 최근의 쓴 수를 지우고, 아닐 경우 해당 수 씀
# 0일 경우 지울 수 있는 수가 있음을 보장(스택이 비어있을 경우)

# 출력: 최종적으로 낸 수의 합
import sys

k = int(input())
stack = []
for i in range(k):
    num = int(sys.stdin.readline())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))
