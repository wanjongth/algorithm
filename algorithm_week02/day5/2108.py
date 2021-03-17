# 통계학
# N 개의 수가 주어졌을 때
# 산술평균, 중앙값, 최빈값, 범위 산출

# 입력 : 첫째 줄에 수의 개수
# 출력 : 산술평균, 중앙값, 최빈값(최빈값이 여러개일 때 두번째로 작은 값),
# 범위 출력 (한 줄에 하나씩)
import sys

n = int(input())

array = list()
for i in range(n):
    integer = int(sys.stdin.readline())
    array.append(integer)

array.sort()


def mean(array):  # 산술평균
    sum = 0
    for i in array:
        sum += i
        mean = sum / len(array)
    return int(mean)


def median(array):  # 중앙값
    mid = int((len(array)+1)/2)
    median = array[mid-1]
    return median


def mode():
    return


def array_range():
    return


print(mean(array))  # 산술평균 출력
print(median(array))  # 중앙값 출력
