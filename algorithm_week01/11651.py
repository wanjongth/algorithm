import sys

case = int(input())
# #받아오기
x_y_list = []

# for _ in range(case):
#     x_y = list(map(int, input().split()))
#     # print(x_y)
#     x_y_list.append(x_y)

# x_y_list.sort(key=lambda x: (x[1], x[0]))

# for i in x_y_list:
#     print(i[0], i[1])


for i in range(case):
    [a, b] = map(int, input().split())
    arr = [b, a]
    x_y_list.append(arr)

x_y_list = sorted(x_y_list)

for b, a in x_y_list:
    print(a, b)
