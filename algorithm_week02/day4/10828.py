# 스택 - 스택
# 정수를 저장하는 스택을 구현, 입력으로 주어지는 명령을 처리하는 프로그램

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 입력 : 첫째줄 - 명령의 개수 N , 둘째 줄부터 명령
# 출력 : 출력해야하는 명령이 주어질 때 마다 한 줄에 하나씩 출력

# 기능 구현 하는 것은 알겠는데, 어떻게 입력받은 값을 넣어줄 것인가.
# 명령어를 입력할때 split으로 나누어 if문으로 비교 - push 연산 때문
import sys
n = int(input())

stack = []
for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.append(command[1])
        # print(stack[-1])
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
