# 딕셔너리 - key, value의 쌍을 데이터로 가지는 자료형
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

# 파이썬의 딕셔너리 자료형은 내부적으로 '해시 테이블'을 이용하므로 데이터의 검색 및 수정에 있어서 O(1)의 시간에 처리 가능

# 딕셔너리에 특정한 원소가 있는지 검사할 때는 '원소 in 딕셔너리'의 형태를 사용할 수 있다.
if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재")

# 딕셔너리와 관련된 함수

# 키 데이터만 담은 리스트
key_list = data.keys()
# 값 데이터만 담은 리스트
value_list = data.values()
print(key_list)
print(value_list)
# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])

# dic.clear()
# key, value 값을 모두 지워준다

# get - Key로 value 얻을 수 있다
print(data.get('사과'))
# dic.get은 dic[key] 처럼 value값을 출력하지만
# 존재 하지 않는 키 호출했을 때 get은 None을, 후자는 에러를 반환한다.

a = dict()
print(a)
