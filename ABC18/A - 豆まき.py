x = []
for i in range(3):
    x.append(int(input()))
sorted_x = sorted(x, reverse=True)
for i in range(3):
    print(sorted_x.index(x[i]) + 1)
