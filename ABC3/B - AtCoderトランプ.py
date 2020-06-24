i = ["a", "b", "d", "G"]
print(list(reversed(i)))  # 1
new_i = list(reversed(i))
new_u = list(sorted(i))
print(new_i)  # 2
print(new_u)  # 3
i.sort()
print(i)  # 4
