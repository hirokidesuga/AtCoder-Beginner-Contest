x = list(map(int, input().split()))
if x.count(x[0]) % 2 == 1:
    print(x[0])
else:
    if x[1] != x[0]:
        print(x[1])
    else:
        print(x[2])