def fullSearch(a, N):
    for i in range(N):
        min_index = i
        for j in range(i, N):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]