
import sys
import heapq
import math

def makeBalanceSearchTree(inHeapQue):
    newHeapQueRight = []
    newHeapQueLeft = []

    length = len(inHeapQue)
    middle = math.floor((length + 1 ) / 2)

    if (length < 1):
        return

    i = 0
    while i < length:
        i = i + 1
        if (i == middle):
            print(heapq.heappop(inHeapQue))
        else:
            if (i < middle):
                element = heapq.heappop(inHeapQue)
                heapq.heappush(newHeapQueLeft, element)
            else:
                element = heapq.heappop(inHeapQue)
                heapq.heappush(newHeapQueRight, element)
    makeBalanceSearchTree(newHeapQueLeft)
    makeBalanceSearchTree(newHeapQueRight)


#put sequens input into a heapque
heapQue = []
for line in sys.stdin:
    element = int(line.strip())
    heapq.heappush(heapQue, element)

#Convertheapque into something that prints a baalnced search tree
makeBalanceSearchTree(heapQue)