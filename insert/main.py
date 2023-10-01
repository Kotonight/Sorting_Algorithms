from random import randint
from insert import ins

N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))

print(a)

ins(a,N)

print(a)
