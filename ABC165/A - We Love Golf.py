x = int(input())
y, z = map(int,input().split())
i = 1
while x * i:
    if x * i > z:
        print("NG")
        exit()
    if y <= x * i <= z:
        print("OK")
        exit()
    i += 1
