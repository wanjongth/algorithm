# 폰켓몬
# N마리의 폰켓몬 중 N/2 뽑기
# 이 중 가장 많은 종류의 폰켓몬을 선택하는 방법 찾아
# 종류 번호의 개수를 return

nums = [3, 1, 2, 3]


def solution(nums):
    answer = 0
    length = len(nums) // 2
    nums.sort()
    last = 0

    for value in nums:
        if(value != last and answer < length):
            answer += 1
            last = value

    return print(answer)


solution(nums)
