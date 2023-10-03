# def bub(N,a):
#     for i in range(N-1):
#         for j in range(N-i-1):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
# def bub(N,a):
#     for n in range(0,N): #upper limit varies based on size of the list
#         temp = 0
#         for i in range(1, N): #keep this for bounds purposes
#             temp = a[i]
#             if a[i] < a[i-1]:
#                 a[i] = a[i-1]
#                 a[i-1] = temp

def bub(arr):
    arr_len = len(arr)
    for i in range(arr_len-1):
        flag = 0
        for j in range(0, arr_len-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                flag = 1
                if flag == 0:
                    break
    return arr