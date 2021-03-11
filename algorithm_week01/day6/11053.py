# N = int(input())
# array = list(map(int, input().split()))
# array.insert(0, 1)
# # print(array)

# memo = []
# # 10 20 10 30 20 50
# for a, b in zip(array, array[1:]):

#     if a < b:
#         memo.append(b)

# print(memo)
# print(len(memo))
# # 위의 코드는 증가하는 부분이 여러개일때 안됨
########################################

import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))

# 구글링
# dp = [0 for i in range(n)]
# # for i in range(n):
# #     for j in range(i):
# #         if a[i] > a[j] and dp[i] < dp[j]: #큰숫자일때만
# #             dp[i] = dp[j]
# #     dp[i] += 1
# # print(max(dp))

# 석진님

dp = [1 for i in range(n)]
for i in range(n):
    # 해당 로직은 오름차순 정렬에 대해 생각해야 수월하다 오름차순 정렬을 하려면
    # 자신보다 왼쪽에 있는 숫자가 자신보다 작아야 오름차순 정렬이다. ex) 2를 기준으로 1,2 => 오름차순O / 2,2 => 오름차순x
    # 2번째 자리보다 작은 숫자가 있어야하는것은 1번째 자리이다. ex) 3번째 자리면 우리는 1부터 3까지의 자리만 비교해주면 된다.
    for j in range(i):
        if a[i] > a[j]:  # ex)i=3 j=0~2  a[3] > a[0~2] => 30 > 10,20,10

            # 하나씩 비교해서 큰게 맞으면 res[i]와 res[j] + 1 중에 큰값을 res[i] 담아준다
            # 이 숫자는 해당 인덱스 번호의 숫자가 가질수 있는 오름차순 정렬 배열 길이 이다 모든 숫자는 자기자신의 오름차순 정렬을 가질수 있기때문에 res={1,1,1,1,1,1}를 해준것!
            # 이말은 숫자를 누적해주기 위함과 바로 왼쪽의 숫자가 자신보다 작은데 가지고 있는 오름차순 정렬 길이가 3이라면 그것보다 큰수인 자신은 당연히 +1개
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))  # 그중 제일 큰것 = 제일 긴 오름차순 길이
