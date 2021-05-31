input = [0, 3, 5, 6, 1, 2, 4]
# 원래의 연산 규칙을 무시하고 *와 +를 써서 제일 큰 값 호출해보아라
# 페이스북 기출문제

def find_max_plus_or_multiply(array):
    multiply_sum = 0
    for num in array :
        if num <= 1 or multiply_sum <=1:
            multiply_sum += num
        else :
            multiply_sum *= num
    return multiply_sum


result = find_max_plus_or_multiply(input)
print(result)