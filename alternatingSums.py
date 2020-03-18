def alternating_sums(arr: list) -> list:
    j = 0
    m, y = [], []

    while j < len(arr):
        if not j % 2:
            m.append(a[j])
        else:
            y.append(a[j])
        j += 1
    return [sum(m), sum(y)]


a = [50, 60, 60, 45, 70]

print(alternating_sums(a))
