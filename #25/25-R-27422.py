for i in range(174457, 174506):
    numdel = 0
    d = []
    for de in range(1, i + 1):
        if i % de == 0:
            d.append(de)
            numdel += 1
            if numdel > 4:
                break
    if numdel == 4:
        print(d[1], d[2])