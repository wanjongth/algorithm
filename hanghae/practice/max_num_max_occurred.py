# 최대값 찾기
# input = [3, 5, 6, 1, 2, 4]


# # def find_max_num(array):
# #     for num in array:
# #         for compare_num in array:
# #             if num < compare_num:
# #                 break
# #         else:
# #             return num


# # result = find_max_num(input)
# # print(result)

# def find_max_num(array):
#     max_num = array[0]
#     for num in array:
#         if num > max_num:
#             max_num = num
#     return max_num


# result = find_max_num(input)
# print(result)

# # 알파벳 빈도수 세기
# input = "hello my name is sparta"


# def find_alphabet_occurrence_array(string):
#     alphabet = [0]*26  # 배열 초기화 [0,0,0,0,0,..]
#     for char in string:
#         if not char.isalpha():  # 알파벳이 아니면 넘어가세요 ex0" "
#             continue
#         arr_index = ord(char) - ord("a")
#         alphabet[arr_index] += 1

#     return alphabet


# result = find_max_occurred_alphabet(input)
# print(result)

# # 최빈값 찾기
# input = "hello my name is sparta"


# def find_max_occurred_alphabet(string):
#     alphabet_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
#                       'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     max_occurence = 0
#     max_alphabet = alphabet_array[0]

#     for alphabet in alphabet_array:
#         occurrence = 0
#         for char in string:
#             if char == alphabet:
#                 occurrence += 1

#         if occurrence > max_occurence:
#             max_occurence = occurrence
#             max_alphabet = alphabet

#     return max_alphabet, max_occurence


# result = find_max_occurred_alphabet(input)
# print(result)


# 최빈값 찾기 2

# 알파벳 빈도수 세기
input = "hello my name is sparta"


def find_alphabet_occurrence_array(string):
    alphabet = [0]*26  # 배열 초기화 [0,0,0,0,0,..]
    for char in string:
        if not char.isalpha():  # 알파벳이 아니면 넘어가세요 ex0" "
            continue
        arr_index = ord(char) - ord("a")
        alphabet[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0

    for index in range(len(alphabet)):
        # index 0 > alphabet 3
        alphabet_occurence = alphabet[arr_index]

        if alphabet_occurence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurence
    # print(max_alphabet_index)
    return chr(max_alphabet_index + ord("a"))


result = find_alphabet_occurrence_array(input)
print(result)
