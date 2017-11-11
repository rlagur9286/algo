def do_fibonacci(num):
    if num <= 1:
        return num
    else:
        return do_fibonacci(num-2) + do_fibonacci(num-1)

if __name__ == '__main__':
    for num in range(8):
        res = do_fibonacci(num)
        print(res)