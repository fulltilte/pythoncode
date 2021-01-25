with open('27687.txt', 'r') as f:
    s = f.read()

k = len(s)
l = 1
lmax = 0

for i in range(k - 1):
    if s[i] == 'Y':
        if s[i + 1] == 'Y':
            l += 1
        else:
            if l > lmax:
                lmax = l
            l = 1
print(lmax)