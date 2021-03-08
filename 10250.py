case = int(input())
data = []
# 로직짜기
# def room_num(H, N):
#     floor = N % H
#     room = N // H + 1
#     if floor == 0: # 반례
#         floor = data[0]
#         room = data[1] // data[0]
#     if room < 10:
#         result = print("%d%d%d" % (floor, 0, room))
#     elif room >= 10:
#         result = print("%d%d" % (floor, room))
#     return result

# 입출력에 맞게 수정..
for _ in range(case):
    data = list(map(int, input().split()))
    # print(data)
    # del data[1]

    floor = data[2] % data[0]
    room = data[2] // data[0] + 1
    if floor == 0:
        floor = data[0]
        room = data[2] // data[0]
    if room < 10:
        result = print("%d%d%d" % (floor, 0, room))
    elif room >= 10:
        result = print("%d%d" % (floor, room))


# 다른코드
# import sys
# import math

# test_data = int(sys.stdin.readline().strip())
# for test in range(test_data):
#     H , W , N = map(int,sys.stdin.readline().strip().split())

#     if N % H != 0:
#         h = N % H
#         w = math.ceil(N/H)
#     else:
#         h = H
#         w = N//H

#     h = str(h)

#     if w <10:
#         w = "0" + str(w)
#     else:
#         w = str(w)

#     result = h + w

#     print(result)
