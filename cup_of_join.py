def cup_of_join(*args, sep='-'):
    res = []

    if args is None:
        print(res)

    for value in args:
        res.extend(value)
        res.append(sep)

    res.pop()
    print(res)


cup_of_join([1, 2], [2, 3], [3, 4])
