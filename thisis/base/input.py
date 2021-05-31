# 알고리즘 문제 풀이의 첫 번째 단계는 데이터를 입력받는 것
# 파이썬에서 데이터를 입력받을 때는 input()을 이용. input()의 경우 한 줄의 문자열을 입력 받도록 해줌
# 입력받은 데이터를 정수형 데이터로 처리하기 위해서는 문자열을 정수로 바꾸는 int() 함수 이용

# 여러 개의 데이터를 입력받을 때는 데이터가 공백으로 구분되는 경우가 많다.
# 그래서 입력받은 문자열을 띄어쓰기로 구부느, 각각 정수 자료형의 데이터로 저장하는 코드의 사용 빈도가 매우 높음
# list(map(int, input().split()))
# input()으로 입력받은 문자열을 split()을 이용해 공백으로 나눈 리스트로 바꾼 뒤에, map을 이용하여 해당 리스트의 모든 원소에 int() 함수를 적용
# 최종적으로 그 결과를 list()로 다시 바꿈으로써 입력받은 문자열을 띄어쓰기로 구분하여 각각 숫자 자료형으로 저장하게 됨

# 입력을 위한 전형적인 소스코드

# 데이터의 개수 입력
n = int(input())
# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

# 공백으로 구분된 데이터의 개수가 많지 않다면, 단순히 map(int, input().split())을 이용하는것도 가능
# 예를 들어 문제에서 첫째 줄에 n, m, k가 공백으로 구분되어 입력된다는 내용이 명시

# n, m, k를 공백으로 구분하여 입력
n, m, k = map(int, input().split())

print(n, m, k)