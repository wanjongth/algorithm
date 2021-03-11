n = int(input())

memo_0 = {0: 0, 1: 1}
memo_1 = {0: 1, 1: 0}

# print(memo)

# 문제 : fibo(0), fibo(1) 이 얼마나 사용되는지
# 어떻게 알 수 있을까


def fibo(n, fibo_memo):
    while n in fibo_memo:
        return fibo_memo[n]

    # print(fibo_memo)

    nth_fibo = fibo(n-1, fibo_memo) + fibo(n-2, fibo_memo)
    fibo_memo[n] = nth_fibo
    # print(fibo_memo)

    return nth_fibo


for i in range(n):
    case = int(input())
    print(fibo(case, memo_1), fibo(case, memo_0))


case_num = int(input())

n_list = []
for i in range(case_num):
    n = int(input())
    n_list.append(n)

# print(n_list)      [0,1,3]


# fibo_memo = {0:[1,0],1:[0,1]}

# def dynamic(n,fibo_memo):
#     if n in fibo_memo:
#         return fibo_memo[n]

#     fibo_count=[]
#     zero_count= dynamic(n-1,fibo_memo)[0]+dynamic(n-2,fibo_memo)[0]
#     one_count= dynamic(n-1,fibo_memo)[1]+dynamic(n-2,fibo_memo)[1]
#     fibo_count.append(zero_count)
#     fibo_count.append(one_count)

#     fibo_memo[n]=fibo_count

#     return fibo_count

# for i in n_list:
#     print(str(dynamic(i,fibo_memo)[0])+" "+str(dynamic(i,fibo_memo)[1]))
