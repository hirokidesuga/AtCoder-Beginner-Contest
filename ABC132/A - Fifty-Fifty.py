x = list(input())
count = 0
for i in x:
    if x.count(i) == 2:
        count += 1
if count == len(x):
    print("Yes")
else:
    print("No")
