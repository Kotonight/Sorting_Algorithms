from random import randint
from fullSearch import fullSearch

N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))

print(a)

fullSearch(a,N)

print(a)