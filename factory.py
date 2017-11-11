def do_factory(num):
    if num <= 1:
        return num
    else:
        return num * do_factory(num-1)

if __name__ == '__main__':
    res = do_factory(3)
    print(res)