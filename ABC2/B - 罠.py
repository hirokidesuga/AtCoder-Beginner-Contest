i = list(input())
x = ['a', 'i', 'u', 'e', 'o']
for o in range(len(i)):
    if i[o] in x:
        i[o] = ''
print(''.join(i))
