# ---------------------------------------------------------
# anagram, 문자열 2개 입력 받아 순열인지 판별하는 메서드
# 참고: https://www.youtube.com/watch?v=u1EPT8RiNW4&list=PLVNY1HnUlO24RlncfRjfoZHnD0YWVsvhq&index=3


def check_anagram(input_str1, input_str2):
    if ''.join(sorted(input_str1.lower())).strip() == ''.join(sorted(input_str2.lower())).strip():
        return True
    else:
        return False

if __name__ == '__main__':
    res = check_anagram(input_str1='as tdfasd', input_str2='AasdST DF')
    print(res)