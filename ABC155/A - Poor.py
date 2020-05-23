x, y, z = map(int, input().split())
if x == y == z or x != y != z and z != x:
    print("No")
else:
    print("Yes")
