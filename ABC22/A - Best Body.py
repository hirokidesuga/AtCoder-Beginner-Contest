x, y, z = map(int, input().split())
n = int(input())
c = [int(input()) for i in range(x-1)]
count = 0
if y <= n <= z:
    count += 1
for i in c:
    n += i
    if y <= n <= z:
        count += 1

print(count)
