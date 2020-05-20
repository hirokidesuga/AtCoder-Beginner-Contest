def main():
    x, y = map(int, input().split())
    if x == y or x < y:
        x += 1
    else:
        y += 1
    return x * y


print(main())
