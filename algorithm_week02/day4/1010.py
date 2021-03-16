# 다리놓기 - 정수론 및 조합론
# 왼쪽 사이트 : N, 오른쪽 사이트 : M
# n<=m 일 때, n개 만큼의 다리를 지으려고 할 때
# 다리끼리는 서로 겹쳐질 수 없음 mCn
# 교차? 상관없음 - Combination
# 조합에서는 (1,3,4) , (3,1,4)를 같은 경우의 수로 본다.
#  1------1       1--  --1
#  2---   2   =   2----  2
#      ---3            --3
#  3------4       4------4

import math
t = int(input())


def Combination(n, k):
    if 0 <= k <= n:
        com = math.factorial(n) / (math.factorial(k)*math.factorial(n-k))
        return int(com)
    else:
        return 0


for i in range(t):
    n, m = map(int, input().split())
    print(Combination(m, n))
