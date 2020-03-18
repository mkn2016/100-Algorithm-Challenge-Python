def add(param1, param2):
    return param1 + param2


def add2(*args):
    return sum(args)


print(add(12, 4))
print(add2(12, 10, 2, 1, 24, 2))
