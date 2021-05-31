import sys

n = int(input())
que = list()
cnt = 0
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        que.append(command[1])
    elif command[0] == 'pop':
        if len(que) > cnt:  # 값이 하나라도 있다면 len(que)는 인덱스 보다 크다
            print(que[cnt])
            cnt += 1
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(que)-cnt)
    elif command[0] == 'empty':  # 리스트가 비어있을 경우
        if len(que) == cnt:  # 현재 인덱스의 값이 len과 같으면
            print(1)
            cnt = 0  # 인덱스 초기화
            que = []  # 리스트 초기화
        else:
            print(0)
    elif command[0] == 'front':
        if len(que) > cnt:
            print(que[cnt])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(que) > cnt:
            print(que[-1])
        else:
            print(-1)
