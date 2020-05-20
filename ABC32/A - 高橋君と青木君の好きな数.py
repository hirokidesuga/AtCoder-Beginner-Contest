def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


x = []
for i in range(3):
    x.append(int(input()))
lcm = x[0] * x[1] / gcd(x[0], x[1])
if x[2] % lcm == 0:
    print(x[2])
else:
    y = (x[2] // lcm) + 1
    print(int(y * lcm))
