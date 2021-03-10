# 입력
H,M = map(int, input().split())

# 문제풀이, 출력
if M > 44: #case1
    print(H,M-45);
elif M < 45 and H>0: #case2
    print(H-1,M+15)
else: # H=0, M < 45
    print(23, M+15)
