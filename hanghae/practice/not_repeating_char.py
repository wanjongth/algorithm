input = "abaddccabaee"
# 위와 같이 영어로 되어있는 문자열이 있을때 반복되지 않는 첫번째 문자를 반환
# 만약 없다면 _ 반환

def find_not_repeating_character(string):
    alphabet = [0]*26  # 배열 초기화 [0,0,0,0,0,..]

    for char in string:
        if not char.isalpha():  # 알파벳이 아니면 넘어가세요 ex0" "
            continue
        arr_index = ord(char) - ord("a")
        alphabet[arr_index] += 1
    
    #하나만 나오는 캐릭터 리스트
    not_repeating_character_array = []

    for index in range(len(alphabet)):
        alphabet_occurence = alphabet[index]
        if alphabet_occurence == 1:
            not_repeating_character_array.append(chr(index + ord("a")))

    #순서
    for char in string:
        if char in not_repeating_character_array:
            return char

    return "_"
    
result = find_not_repeating_character(input)
print(result)