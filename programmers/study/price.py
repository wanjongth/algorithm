# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때,
# 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

def solution(prices):
    answer = []

    for i in range(len(prices)):
        cnt = 0
        for j in prices[i:]:
            if prices[i] <= j:
                cnt += 1

        answer.append(cnt-1)

    return answer


print(solution([1, 2, 3, 2, 3]))
# 테스트 케이스
print(solution([1, 2, 3, 2, 3, 1]))
# return -> 5 4 1 2 1 0
