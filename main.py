import time
from random import randint
from bubble import bubble
from fullSearch import fullSearch

def getAlgorythmTimeForBubble(array, capacity):

    start = time.time()

    bubble.bub(capacity, array)

    end = time.time()

    return end - start

def getAlgorythmTimeForFullSearch(array, capacity):

    start = time.time()

    fullSearch.fullSearch(array, capacity)

    end = time.time()

    return end - start

capacities = [10, 100, 1000, 10000]
bubbleTimes = []
fullSearchTimes = []

for capacity in capacities:

    a = []
    for i in range(capacity):
        a.append(randint(1, 99))

    print("Chech time for ", capacity)

    bubbleTimes.append(getAlgorythmTimeForBubble(a.copy(), capacity))
    fullSearchTimes.append(getAlgorythmTimeForFullSearch(a.copy(), capacity))

print("Bubble times")
print(bubbleTimes)

print("FullSearch times")
print(fullSearchTimes)