# 잃어버린 괄호 - 그리디
# 오늘 할 문제는 아니지만 같은 그리디로 분류되어 있어 추가로 진행

# +,-,괄호를 가지고, 괄호를 적절히 쳐서 최소값을 만드는 프로그램

# 입력 - 식(0~9와 +,-로만 이루어짐) 가장 처음과 마지막 문자는 숫자,
# 연속한 연산자는 나오지 않고, 5자리보다 많이 연속되는 숫자는 없다.
# 출력 : 최솟값 출력

# 내생각
# +가 나오는 곳 양 옆의 숫자를 더하면 된다
# 어떻게 판단?
# 받아온 스트링을 -로 슬라이싱하고
# sum 해주고 순서대로 계산해줌

array = input().split('-')
num = []
for i in array:
    cnt = 0
    second_array = i.split('+')  # +로 구분해주고
    for j in second_array:  # 그걸 하나씩 돌면서 cnt에 놔준다. !! (이 부분 헷갈렸음)
        cnt += int(j)
        # print(int(j))
        # print(cnt)
    num.append(cnt)
# print(num)
n = num[0]  # 첫번째 원소
for i in range(1, len(num)):
    n -= num[i]  # 첫번째 원소를 더해주고 뒤부터는 빼준다
print(n)
