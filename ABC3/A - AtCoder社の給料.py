x = int(input())


def main():
    ave = 0
    for i in range(x):
        ave += (i + 1) * 10000 * 1 / x
    return int(ave)


print(main())
