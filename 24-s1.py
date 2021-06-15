f = open('24-s1.txt', 'r')
count = 0
for x in f.readlines():
    a = True
    for i in range(len(x) - 2):
        if x[i] == 'A' and x[i + 2] == 'R':
            a = False
    if a == False:
        count += 1
print(count)