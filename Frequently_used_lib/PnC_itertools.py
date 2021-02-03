from itertools import permutations, combinations, product, combinations_with_replacement

# 반복되는 데이터를 처리하는 기능 포함 - permutations, combinations ..

# permutations - r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열) nPr

data = ['A', 'B', 'C']
result = list(permutations(data, 2))

print(result)

# combinations - r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합) nCr

result = list(combinations(data,2))
print(result)

# product - r개의 데이터를 뽑아 일렬로 나열(순열). 다만 원소를 중복하여 뽑는다.
result = list(product(data, repeat=2))
print(result)

# combinations_with_replacement - 말 그대로 중복을 허용한 조합
result = list(combinations_with_replacement(data, 2))
print(result)