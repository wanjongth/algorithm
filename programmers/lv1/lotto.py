# 로또를 구매한 민우는 당첨 번호 발표일을 학수고대하고 있었습니다.
# 하지만, 민우의 동생이 로또에 낙서를 하여, 일부 번호를 알아볼 수 없게 되었습니다.
# 당첨 번호 발표 후, 민우는 자신이 구매했던 로또로 당첨이 가능했던 최고 순위와 최저 순위를 알아보고 싶어 졌습니다.

def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zero_cnt = lottos.count(0)

    for i in lottos:
        if i in win_nums:
            cnt += 1

    total = cnt + zero_cnt

    # 6이면 1, 5면 2, 4면 3, 3이면 4, 2면 5 그 외 6 ->

    # 최고
    if total > 1:
        answer.append(7 - (cnt+zero_cnt))
    else:
        answer.append(6)

    # 최저
    if cnt == 0:
        answer.append(6)
    else:
        answer.append(7-cnt)

    return answer


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
# [3, 5]

# 다른 사람 풀이


def solution(lottos, win_nums):

    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans], rank[ans]
