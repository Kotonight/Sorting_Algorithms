import random

def qui(a, l, r):
    if l >= r:
        return 
    else:
        q = random.choice(a[l:r + 1])
        i = l
        j = r
        while i <= j:
            while a[i] < q:
                i += 1
            while a[j] > q:
                j -= 1
            if i <= j: 
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1 
                qui(a, l, j)
                qui(a, i, r)