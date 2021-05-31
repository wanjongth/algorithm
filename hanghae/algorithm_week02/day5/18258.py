# 큐2 - 큐  # 10828 스택이랑 같은 문제
# 정수를 저장하는 큐 구현
# 입력 - 첫째 줄 : 명령의 수, 둘째 줄 - 명령

# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 방법 1
import sys
import collections

n = int(input())
# que = list()
que = collections.deque()
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        que.append(command[1])
    elif command[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            # que.sort(reverse=True)
            # pop = que.pop()
            # print(pop)
            # que.sort(reverse=True)
            pop = que.popleft()
            print(pop)
    elif command[0] == 'size':
        print(len(que))
    elif command[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif command[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
