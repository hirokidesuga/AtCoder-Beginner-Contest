x, y = map(int, input().split())
if (x + y) % 2 != 0:
    print((x + y) // 2 + 1)
else:
    print((x + y) // 2)
