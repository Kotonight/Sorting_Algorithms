from random import randint
from quick import qui

N = 10
a = []
l=0
r=N-1
for i in range(N):
    a.append(randint(1, 99))

print(a)

qui(a,l,r)

print(a)
