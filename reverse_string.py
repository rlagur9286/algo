# ---------------------------------------------------------
# 문자열 뒤집기 알고리즘
# 참고: https://www.youtube.com/watch?v=7yMk8tnHWHU&list=PLVNY1HnUlO24RlncfRjfoZHnD0YWVsvhq&index=2


def reverse_string(input_string):
    stack = []
    result = ""

    for ch in input_string:
        stack.append(ch)

    while len(stack) > 0:
        result += stack.pop()
    return result

if __name__ == '__main__':
    res = reverse_string('가나다라마바사')
    print(res)
