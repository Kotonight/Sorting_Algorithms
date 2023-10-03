import random

# def qui(a, l, r):
#     if l >= r:
#         return 
#     else:
#         q = random.choice(a[l:r + 1])
#         i = l
#         j = r
#         while i <= j:
#             while a[i] < q:
#                 i += 1
#             while a[j] > q:
#                 j -= 1
#             if i <= j: 
#                 a[i], a[j] = a[j], a[i]
#                 i += 1
#                 j -= 1 
#                 qui(a, l, j)
#                 qui(a, i, r)

def qui(a):
    """Given indexable and slicable iterable, return a sorted list"""
    if a: # if given list (or tuple) with one ordered item or more: 
        pivot = a[0]
        # below will be less than:
        below = [i for i in a[1:] if i < pivot] 
        # above will be greater than or equal to:
        above = [i for i in a[1:] if i >= pivot]
        return qui(below) + [pivot] + qui(above)
    else: 
        return a # empty list