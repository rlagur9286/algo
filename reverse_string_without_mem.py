def reverse_string_without_mem(string):
    if len(string) == 0:
        return False
    str_len = len(string)
    i = 0
    string = list(string)
    while i < int(str_len/2):
        string[i], string[str_len-1-i] = string[str_len-1-i], string[i]
        i += 1
    return ''.join(string)

if __name__ == '__main__':
    ori_str = '한글은 되려나'
    result = reverse_string_without_mem(string=ori_str)
    print('Original : ', ori_str)
    print('Reversed : ', result)

    from anagram import check_anagram
    print(check_anagram(ori_str, result))