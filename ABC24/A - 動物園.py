w, x, y, z = map(int, input().split())
o, p = map(int, input().split())
count = w * o + x * p
if (o + p) >= z:
    count -= (o + p) * y
print(count)
