# 프로그램의 흐름 제어
x = 15
if x >= 10:
    print(x)

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

# 조건문의 값이 참이라 해도, 아무것도 처리하고 싶지 않을 때 - pass
if score >= 80:
    pass
else:
    print('성적 80점 미만')
print('프로그램을 종료합니다')

# 조건문에서 실행될 소스코드가 한 줄인 경우, 줄바꿈을 하지 않고도 간략하게 표현 가능
if score >=80 : result = "success"
else : result = "Fail"
print(result)

# 조건부 표현식
result = "Success" if score >= 80 else "fail"
print(result)

# 조건부 표현식의 활용 - 리스트에 있는 원소의 값을 변경해서, 또 다른 리스트를 만들고자 할 때
# case1
a = [1, 2, 3, 4, 5, 5, 5,]
remove_set = {3, 5}

result = []
for i  in a:
    if i not in remove_set:
        result.append(i)
print(result)
# case2
a = [1, 2, 3, 4, 5, 5, 5,]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)

# 파이썬에서는 조건문 안에서 수학의 부등식을 그대로 사용 가능
# x > 0 and x < 20    ==   0 < x < 20
