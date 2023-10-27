def sort_g(ls):
    n, i = len(ls), 0
    while True:
        if i + 1 == n:
            break
        if ls[i + 1] >= ls[i]:
            i += 1
        else:
            ls[i], ls[i + 1] = ls[i + 1], ls[i]
            if i > 0:
                i -= 1
            else:
                i += 1
    return ls