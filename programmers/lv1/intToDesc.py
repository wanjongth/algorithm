# 함수 solution은 정수 n을 매개변수로 입력받습니다.
# n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
# 예를들어 n이 118372면 873211을 리턴하면 됩니다.

def solution(n):
    array = []
    n = str(n)

    for i in n:
        array.append(i)
    array.sort(reverse=True)
    answer = ''.join(array)
    return int(answer)


print(solution(123455))

# 정수를 어떻게 리스트로 변환할까 생각하다가 위처럼 풀었는데,
# 리스트 선언과 동시에 str(n)을 넣어주면 된다;;


def solution(n):
    ls = list(str(n))
    ls.sort(reverse=True)
    return int("".join(ls))
