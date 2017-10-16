# ---------------------------------------------------------
# 같은 문자 반복 횟수를 이용한 문자열 압축
# 시간 복잡도: O(N)
# 공간 복잡도: O(N)
# 참조: https://www.youtube.com/watch?v=y4-t0bzAB6o&list=PLVNY1HnUlO24RlncfRjfoZHnD0YWVsvhq&index=6


def compress_string(input_string):
    buffer = ""
    cnt = 1
    result = ""

    for ch in input_string:
        if buffer == "":
            buffer = ch
        elif buffer == ch:
            cnt += 1
        else:
            result += buffer
            result += str(cnt)
            buffer = ch
            cnt = 1
    result += buffer
    result += str(cnt)

    if len(result) < len(input_string):
        return result
    else:
        return input_string

if __name__ == '__main__':
    res = compress_string('aabccccccccaaa')
    print(res)
