x, y = map(int, input().split())
if y % x != 0:
    print(int(y/x)+1)
else:
    print(int(y/x))
