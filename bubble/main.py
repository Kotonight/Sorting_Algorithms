from random import randint
from bubble import bub

N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))

print(a)

bub(N,a)

print(a)
