# H-Index - 정렬 - 42747
'''
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. H-Index는 다음과 같이 구합니다.
어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.
'''

# 위키 나온대로 해결 - 11번 케이스 불통과


def solution(citations):
    if sum(citations) == 0:
        return 0
    h = 0

    citations.sort(reverse=True)

    for i, v in enumerate(citations):
        if i <= v:
            h = i

    # if max(citations) < h+1:
    #     return max(citations)

    return h+1


print(solution([3, 0, 6, 1, 5]))
print(solution([5, 5, 5, 5]))
print(solution([2, 2, 2, 2]))
