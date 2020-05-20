x, y = map(int, input().split())
if y % (x / 4) == 0:
    print("4:3")
else:
    print("16:9")