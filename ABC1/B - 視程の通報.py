x = int(input())
y = x / 1000
if y < 0.1:
    print(str().zfill(2))
elif y <= 5:
    y = int(y * 10)
    print(str(y).zfill(2))
elif 6 <= y <= 30:
    print(int(y)+50)
elif 35 <= y <= 70:
    print(int((y-30)/5+80))
else:
    print(89)

