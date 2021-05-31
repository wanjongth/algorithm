# 색종이 만들기 - 분할정복(쿼드 트리)
# 정사각형 칸들로 이루어진 정사각형 모양 종이
# 하얀색이나 파란색으로 칠해져 있을 때 일정한 규칙에 따라 다양한 크기를 가진
# 정사각형 모양의 하얀색 또는 파란색 색종이를 만들려고 함.

# 입력: 첫째줄 - N 둘째줄부터 - 색종이
# 출력: 첫째줄 - 하얀색 색종이, 둘째줄 - 파란색 색종이

# import sys

# n = int(input())
# paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# result = []


# def solution(x, y, n):
#     color = paper[x][y]  # 첫 색깔
#     for i in range(x, x+n):
#         for j in range(y, y+n):
#             if color != paper[i][j]:  # i,j들이 첫색깔과 같지 않다면
#                 solution(x, y, n//2)  # 2사분면
#                 solution(x, y+n//2, n//2)  # 3사분면
#                 solution(x+n//2, y, n//2)  # 1사분면
#                 solution(x+n//2, y+n//2, n//2)  # 4사분면
#                 return
#     if color == 0:
#         result.append(0)
#     else:
#         result.append(1)


# solution(0, 0, n)
# print(result.count(0))
# print(result.count(1))

import sys
input = sys.stdin.readline
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0


def check(i, j, d):  # 해당 범위의 색이 모두 같은 지 검사
    color = paper[i][j]  # 첫 색깔
    for x in range(i, i+d):
        for y in range(j, j+d):
            if paper[x][y] != color:  # x,y들이 모두 첫 색깔과 같지 않다면
                return False
    return True
