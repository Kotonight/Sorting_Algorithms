import time
from random import randint
from bubble import bubble
from fullSearch import fullSearch
from quick import quick
from insert import insert
from comb import comb
from gnome import sort_g
from heap import heap_sort
from shaker import shaker

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

def getAlgorythmTimeForComb(array):

    start = time.time()

    comb(array)

    end = time.time()

    return end - start

def getAlgorythmTimeForGnome(array):

    start = time.time()

    sort_g(array)

    end = time.time()

    return end - start

def getAlgorythmTimeForHeap(array):

    start = time.time()

    heap_sort(array)

    end = time.time()

    return end - start

def getAlgorythmTimeForShaker(array):

    start = time.time()

    shaker(array)

    end = time.time()

    return end - start

capacities = [10, 100, 1000, 10000, 50000]
bubbleTimes = []
fullSearchTimes = []
quickTimes = []
insertTimes = []
combTimes = []
gnomeTimes = []
heapTimes = []
shakerTimes = []

for capacity in capacities:

    a = []
    for i in range(capacity):
        a.append(randint(1, 99))

    print("Chech time for ", capacity)

    bubbleTimes.append(getAlgorythmTimeForBubble(a.copy()))
    fullSearchTimes.append(getAlgorythmTimeForFullSearch(a.copy(), capacity))
    quickTimes.append(getAlgorythmTimeForQuick(a.copy()))
    insertTimes.append(getAlgorythmTimeForInsert(a.copy(), capacity))
    combTimes.append(getAlgorythmTimeForComb(a.copy()))
    gnomeTimes.append(getAlgorythmTimeForGnome(a.copy()))
    heapTimes.append(getAlgorythmTimeForHeap(a.copy()))
    shakerTimes.append(getAlgorythmTimeForShaker(a.copy()))

print("Bubble times", bubbleTimes, "FullSearch times", fullSearchTimes, "Quick times", quickTimes, "Insert times", insertTimes, "Comb times", combTimes, "Gnome times", gnomeTimes, "Heap times", heapTimes, "Shaker times", shakerTimes, sep="\n")