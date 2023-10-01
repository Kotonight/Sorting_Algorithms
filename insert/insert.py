def ins(a,N):
    for i in range(N):
        key = a[i]
        j = i-1
        while j >=0 and key < a[j] :
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key 
