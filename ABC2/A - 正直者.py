def main():
    x, y = input().split(" ")
    if int(x) > int(y):
        return x
    else:
        return y


print(main())
