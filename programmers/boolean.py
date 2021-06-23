# 볼때마다 헷갈려서 한번 정리.
# 조건문, while문의 조건 같은 경우에 불리언 타입을 사용하는 경우.

# True
list = []

if list == []:
    print(True)
if len(list) == 0:
    print(True)
if not list:
    print(True)

# False
if list != []:
    print(False)
if len(list) != 0:
    print(False)
if list:
    print(False)
