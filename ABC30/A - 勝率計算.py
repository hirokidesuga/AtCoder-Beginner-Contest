w, x, y, z = map(int, input().split())
if x/w == z/y:
    print("DRAW")
elif x/w > z/y:
    print("TAKAHASHI")
else:
    print("AOKI")
