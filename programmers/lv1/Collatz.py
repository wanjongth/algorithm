# 주어진 수가 1이 될때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측입니다.
# 1-1. 입력된 수가 짝수라면 2로 나눕니다.
# 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
# 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
# 위 작업을 몇 번이나 반복해야하는지 반환하는 함수, solution을 완성해 주세요. 단, 작업을 500번을 반복해도 1이 되지 않는다면 –1을 반환해 주세요.
def solution(num):
    cnt = 0

    while True:
        if num == 1:
            break
        elif num % 2 == 0:
            num /= 2
            cnt += 1
        elif num % 2 != 0:
            num = num*3 + 1
            cnt += 1
        if cnt > 501:
            cnt = -1
            break
    return cnt


print(solution(6))
print(solution(626331))
