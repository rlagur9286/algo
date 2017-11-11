def sum_btw_two_numbers(num1, num2):
    sum = 0
    for i in range(num1, num2+1):
        sum += i
    return sum


def sum_btw_two_numbers_v2(num1, num2):
    # 두 수 사이의 모든 수의 합 공식
    # (시작수 + 끝수) * 총 개수 / 2
    return (num1 + num2) * (num2 - num1 + 1) / 2

if __name__ == '__main__':
    res = sum_btw_two_numbers(8, 15)
    print(res)
    res = sum_btw_two_numbers_v2(8, 15)
    print(res)
