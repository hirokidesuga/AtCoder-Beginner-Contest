x = list(input())
w = int(input())
y = []
for i in range(5):
    for j in range(5):
        y.append(x[i] + x[j])
print(y[w-1])
