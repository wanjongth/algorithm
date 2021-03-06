words = input().upper()#words 받기
alpabhet = list(set(words))# 집합에 넣음(중복 제거)
#print(alpabhet)
count_word = []#카운트 할 빈 리스트

for word in alpabhet:#집합을 돌면서
    count_word.append(words.count(word)) # 리스트의 원소들 따로 숫자 세기 (몰랐던 부분)
print(count_word)

if count_word.count(max(count_word))>=2:
    print('?')
else:
    print(alpabhet[count_word.index(max(count_word))])#index (몰랐던 부분)


# #코드2
# from collections import Counter

# word = list(input().lower())

# reverse_dict = dict(map(reversed, Counter(word).items()))
# valuelist = list(Counter(word).values())

# max = max(valuelist)

# if valuelist.count(max) == 1:
#     print(reverse_dict.get(max).upper())
# else:
#     print("?")
