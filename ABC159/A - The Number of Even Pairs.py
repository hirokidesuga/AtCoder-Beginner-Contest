a = list(map(int, input().split()))


def a1():
    if a[0] == 1 or a[0] == 0:
        a[0] = 0
        return a[0]
    else:
        return a[0] * (a[0] - 1) / 2


def b1():
    if a[1] == 1 or a[1] == 0:
        a[1] = 0
        return a[1]
    else:
        return a[1] * (a[1] - 1) / 2


print(int(a1() + b1()))