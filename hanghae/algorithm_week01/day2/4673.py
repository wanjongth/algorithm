def self_num_check(n):
    return n + n//1000 + n//100%10 + n//10%10 + n%10
    # return n + n//10 + n%10

create_num = []
# array = [i for i in range(100)]
array = [i for i in range(10000)]
self_num=[]

# for i in range(100):
for i in range(10000):
    # print(self_num_check(i))
    # if self_num_check(i) < 100:
    if self_num_check(i) < 10000:
        print(self_num_check(i))
        create_num.append(self_num_check(i))
        
self_num=list(set(array)-set(create_num))
self_num = sorted(self_num)

for i in self_num:
    print(i)


# #코드2
# list=[]

# for n in range(1,10000):
#     def d(n):
#         return n + n//1000 + (n//100)%10 + (n//10)%10 + n%10
#     list.append(d(n))

# for n in range(1,10000):
#     # 리스트에 없는 함수 불러오기
#     Result = n in list
#     if Result is False:
#         print(n)

# n_list=[]
# # for i in range(0,10000):
# #     n_list.append(i+sum(list(map(int,i))))                  
# # print(n_list)

# n_list = [i+sum(list(map(int,str(i)))) for i in range(0,10000)]  #int를 바로 list로 넣으려면 다시 리스트를 만들어야한다?

# for i in range(0,10001):
#     if i not in n_list:
#         print(i)