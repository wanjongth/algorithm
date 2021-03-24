# 시각 - 완전탐색
# 정수 N이 입력되면 00시 00분 00초 부터 N시 59분 59초까지의 모든 시각중에서 3이 하나라도 포함되는 경우의 수 구하는 프로그램

# 입력 : 정수 N
# 출력 : 조건에 맞는 경우의 수

n = int(input())

# 내 생각 - 시 분 초 별로 포함되어 있으면 cnt 증가..
# 뭐가 잘못 된건지 모르겠다 ..


def time(n):
    cnt = 0
    for h in range(n+1):
        if h == 3 or h == 13:
            cnt += 1
        for m in range(60):
            if m % 10 == 3 or m // 10 == 3:
                cnt += 1
            for s in range(60):
                if s % 10 == 3 or s // 10 == 3:
                    cnt += 1
    return cnt

# 책 내용 - 문자열 변환 후 합치고 3이 포함되어 있으면 cnt 증가


def time2(n):
    cnt = 0
    for h in range(n+1):
        for m in range(60):
            for s in range(60):
                if '3' in str(h) + str(m) + str(s):
                    cnt += 1
    return cnt


print(time(n))
print(time2(n))
