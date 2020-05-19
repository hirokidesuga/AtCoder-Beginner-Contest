o = []


def q(x, y):
    for m in range(x):
        o.append(y)


t = int(input())

p = [1, 2, 4, 8]
l = len(p)

count = 0
for i in range(l):
    if t // p[l - 1 - i] != 0:
        count += t // p[l - 1 - i]
        q(t // p[l - 1 - i], p[l - 1 - i])
        t -= p[l - 1 - i] * (t // p[l - 1 - i])
    if t == 0:
        break

print(count)
for i in o:
    print(i)