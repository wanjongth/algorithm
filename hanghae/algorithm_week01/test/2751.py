import sys
# 첫째줄에 n, n 개의 숫자가 한줄씩 입력
# 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력
n = int(input())
array = list()
for _ in range(n):
    # 처음엔 input()으로 받았으나 시간 줄이기 위해 sys.stdin.readline 사용
    array.append(int(sys.stdin.readline()))

array.sort()

for i in range(n):
    print(array[i])
