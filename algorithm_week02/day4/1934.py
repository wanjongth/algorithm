# 최소공배수 - 정수조합론
# 2609번을 풀고, 입력받는 방식만 바꿔주면 되는 문제

# 입력 : 첫째줄 - 테스트케이스 , 둘째줄 - A, B
# 출력 : A와 B의 최소공배수를 입력받은 순서대로 하나씩 출력
import math

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    gcd = math.gcd(a, b)
    lcm = gcd * a/gcd * b/gcd
    print(int(lcm))
