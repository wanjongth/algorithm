# 문자인지 확인
# print("a".isalpha())

input = "Hello my name is jongwan"


def find_max_occurred_alphabet(string):
    alphabet_list = [0]*26

    for char in string:
        if not char.isalphabet():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_list[arr_index] += 1

        return alphabet_list


result = find_max_occurred_alphabet(input)
print(result)
