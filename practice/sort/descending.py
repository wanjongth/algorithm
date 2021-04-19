# 위에서 아래로
# 다양한 수가 크기에 상관없이 나열되어 있다. 큰 수부터 작은 수의 순서로 정렬해야 한다.
# 수열을 내림차순으로 정렬하는 프로그램을 만드시오

# 입력 : 첫째 줄에 수열에 속해 있는 수의 개수 N
# 둘째 줄부터 N 개의 수가 입력

# 출력 : 공백으로 구분하여 출력
# 범위가 1 <= N <= 100,000으로 매우 작음 --> 아무 정렬 알고리즘이나 선택해도 상관 없다

# 입력 예
# 3
# 15
# 27
# 12

n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

# print(array)

array.sort(reverse=True)
for i in array:
    print(i, end=' ')

# for문 안에 print 쓸 때
# end= ' ' -> 자주 쓰이는 것 같으니 기억해두자

# 풀이 2
array = sorted(array, reverse=True)
for i in array:
    print(i, end=' ')
