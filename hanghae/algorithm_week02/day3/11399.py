# ATM - 그리디
# ATM이 한 대, 앞에 N명의 사람들이 줄을 서있음.
# i 번 사람이 돈을 인출하는데 걸리는 시간은 Pi

# 사람들이 돈을 인출하는데 필요한 시간의 합 최솟값

# 입력 : 첫째줄 - N, 둘째줄 - 각 사람이 인출하는데 필요한 시간
# 아이디어!
# 들어온 입력을 내림차순 정렬해주고,(왜 내림차순인지는 뒤에서)
# 큰 숫자는 1 곱하고, 그다음 큰 숫자는 2, .... ,제일 작은 숫자는 n을 곱해준다


n = int(input())
times = list(map(int, input().split()))
times.sort(reverse=True)

result = 0
for index, time in enumerate(times):
    # print(index) # 0,1,2,3,4
    # print(time) # 4,3,3,2,1
    result += (index+1) * time
print(result)

# 방법 2
# wait_time = 0
# sum_time = 0
# for i in time:
#     wait_time += i
#     sum_time += wait_time
# print(sum_time)

# for i, v in enumerate(t):
#     print("index : {}, value: {}".format(i,v))
# ...
# index : 0, value: 1
# index : 1, value: 5
