# 입력
# a = list(map(int,input()))
# b = list(map(int,input()))

# 변수 확인
# print(a[0],a[1],a[2],b[0],b[1],b[2])

# 풀이
# c = a[0]*b[2]*100+a[1]*b[2]*10+a[2]*b[2]
# d = a[0]*b[1]*100+a[1]*b[1]*10+a[2]*b[1]
# e = a[0]*b[0]*100+a[1]*b[0]*10+a[2]*b[0]
# f = c+d*10+e*100

# #출력
# print(c)
# print(d)
# print(e)
# print(f)

#입력2
a = input()
b = input()
a = int(a)
b = int(b)

#풀이+출력2
print(a * (b%10))
print(a * (b//10%10))
print(a * (b//100))
print(a * b)

# # 코드2
# # 변수 입력
# a = input()
# b = input()

# # 변수설정
# a = int(a)
# b = b # indexing 해야 해서 문자열로 유지
# c = int(b[2])
# d = int(b[1])
# e = int(b[0])

# # 값 출력
# print(a*c)
# print(a*d)
# print(a*e)
# print(a*c+(a*d*10)+(a*e*100))

# # 코드3
# a = int(input())
# b = list(map(int,input()))

# for i in range(3):
#     print(a*b[2-i])    
# print(a*b[2]+a*b[1]*10+a*b[0]*100)