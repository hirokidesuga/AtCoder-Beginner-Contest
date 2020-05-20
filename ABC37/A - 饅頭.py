x, y, z = map(int, input().split())
if x >= y:
    print(z//y)
else:
    print(z//x)