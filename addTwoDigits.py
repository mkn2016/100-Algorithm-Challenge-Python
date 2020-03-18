def add_two_digits(n: int) -> int:
    return sum([int(x) for x in list(str(n))])

print(add_two_digits(29))