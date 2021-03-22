# 8*8 좌표 평면에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수
# 나이트 - 수평으로 두칸 이동한 뒤에 수직으로 한칸 이동
#      - 수직으로 두칸 이동한 뒤에 수평으로 한칸 이동
# 행 위치 - 1~8 표현, 열 위치 - a~h 표현

# 입력 : 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열
# 나이트가 이동할 수 있는 경우의 수(2~8)

current = input()
row = int(current[1])
col = int(ord(current[0]) - int(ord('a')) + 1)
# print(row, col)

# 아래, 오른쪽 : 양수 ##  위, 왼쪽 : 음수
steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
         (1, -2), (1, 2), (2, -1), (2, 1)]

cnt = 0

for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]
    # 범위를 넘어가지 않는다면 카운트
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        cnt += 1

print(cnt)
