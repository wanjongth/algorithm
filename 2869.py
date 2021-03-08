import math

A, B, V = map(int, input().split())

# 식 일반화, math를 import하고 ceil을 쓰면
# round = 반올림, ceil = 올림
# 내림 = int(float('2.12134'))
days = math.ceil((V-A)/(A-B))+1

print(days)
