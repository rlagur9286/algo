# ---------------------------------------------------------
# 문자열에 포함된 문자들이 전부 유일한 지 검사하는 알고리즘
# 제한 사항: list나 set 같은 자료구조 사용 불가
# 시간 복잡도: O(N)
# 공간 복잡도: O(N)


def check_duplicated_without_data_structure(input_string):
    if len(input_string) > 256:
        return False

    check_arr = [False] * 256

    for ch in input_string:
        if check_arr[ord(ch)] is True:
            return False
        else:
            check_arr[ord(ch)] = True
    return True


def check_duplicated_with_data_structure(input_string):
    input_string_set = set(input_string)
    if len(input_string) != len(input_string_set):
        return False
    else:
        return True


if __name__ == '__main__':
    result = check_duplicated_without_data_structure(input_string='asfdgeq;')
    print(result)

    result = check_duplicated_with_data_structure(input_string='asfdgeq;')
    print(result)
