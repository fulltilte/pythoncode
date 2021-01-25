def F(start, end):
    if end < start:
        return 0
    if end == start:
        return 1
    k = F(start, end - 1)
    if end % 2 == 0:
        k += F(start, end // 2)
    return k
print(F(1, 10) * F(10, 20))