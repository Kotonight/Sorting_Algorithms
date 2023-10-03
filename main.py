import time
from random import randint
from bubble import bubble
from fullSearch import fullSearch
from quick import quick
from insert import insert

def getAlgorythmTimeForBubble(array):

    start = time.time()

    bubble.bub(array)

    end = time.time()

    return end - start

def getAlgorythmTimeForFullSearch(array, capacity):

    start = time.time()

    fullSearch.fullSearch(array, capacity)

    end = time.time()

    return end - start

def getAlgorythmTimeForQuick(array):

    start = time.time()

    quick.qui(array)

    end = time.time()

    return end - start

def getAlgorythmTimeForInsert(array, capacity):

    start = time.time()

    insert.ins(array, capacity)

    end = time.time()

    return end - start

capacities = [10, 100, 1000, 10000]
bubbleTimes = []
fullSearchTimes = []
quickTimes = []
insertTimes = []

for capacity in capacities:

    a = []
    for i in range(capacity):
        a.append(randint(1, 99))

    print("Chech time for ", capacity)

    bubbleTimes.append(getAlgorythmTimeForBubble(a.copy()))
    fullSearchTimes.append(getAlgorythmTimeForFullSearch(a.copy(), capacity))
    quickTimes.append(getAlgorythmTimeForQuick(a.copy()))
    insertTimes.append(getAlgorythmTimeForInsert(a.copy(), capacity))

print("Bubble times", bubbleTimes, "FullSearch times", fullSearchTimes, "Quick times", quickTimes, "Insert times", insertTimes, sep="\n")