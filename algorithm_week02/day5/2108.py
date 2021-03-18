# 통계학
# N 개의 수가 주어졌을 때
# 산술평균, 중앙값, 최빈값, 범위 산출

# 입력 : 첫째 줄에 수의 개수
# 출력 : 산술평균, 중앙값, 최빈값(최빈값이 여러개일 때 두번째로 작은 값),
# 범위 출력 (한 줄에 하나씩)
import sys
from collections import Counter

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
    return round(mean)  # 반올림하여 출력


def median(array):  # 중앙값
    mid = int((len(array)+1)/2)
    median = array[mid-1]
    return median


def mode(array):
    C = Counter(array)  # collection의 카운터 모듈, 요소의 출현 횟수를 나타내준다
    order = C.most_common()  # most_common을 쓰면 많이 출현하는 애들을 나타내준다
    print(order)
    maximum = order[0][1]

    mode = []
    for num in order:
        if num[1] == maximum:
            mode.append(num[0])
    print(mode)
    if len(mode) == 1:  # 최빈값이 하나일 때
        return mode[0]
    else:  # 최빈값이 여러개일때
        return mode[1]  # 두번째 값 출력


def array_range(array):
    range = array[-1] - array[0]
    return range


print(mean(array))  # 산술평균 출력
print(median(array))  # 중앙값 출력
print(mode(array))  # 최빈값 출력
print(array_range(array))  # 범위 출력
