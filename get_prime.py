import math


def check_prime(n):
    root_n = int(math.sqrt(n)) + 1
    for i in range(2, root_n):
        if n % i == 0:
            return False
    return True


def get_prime_all(n):
    root_n = int(math.sqrt(n)) + 1
    arr = [0] * n
    for i in range(2, root_n):
        if arr[i] == 1:
            continue
        j = 2 * i
        while j < n:
            arr[j] = 1
            j += i
    # for i in range(2, n):
    #     if arr[i] == 0:
    #         print(i, arr[i])

if __name__ == '__main__':
    import time
    start = time.time()
    result = check_prime(113)
    end = time.time()
    print(result, end - start)

    start = time.time()
    get_prime_all(10000000)
    end = time.time()
    print(end - start)
