import math

x = int(input())
y = int(input())
if x % y != 0:
    print((math.floor(x / y) + 1) * y - x)
else:
    print(0)
