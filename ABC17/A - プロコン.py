count = 0
for i in range(3):
    x, y = map(int, input().split())
    count += x * y / 10
print(int(count))
