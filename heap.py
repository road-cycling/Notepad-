class Heap:

    def __init__(self):
        self._heap = []

    def heapSort(self):

        newArray = []

        top = self.removeTop()
        while top != False:
            newArray.append(top)

            top = self.removeTop()

        return newArray

    def insert(self, item):

        self._heap.append(item)

        atIndex = len(self._heap) - 1

        while atIndex != 0:

            parentIndex = atIndex // 2

            if self._heap[parentIndex] > self._heap[atIndex]:
                self._heap[atIndex] = self._heap[parentIndex]
                self._heap[parentIndex] = item
            else:
                break

            atIndex = parentIndex
                

    def removeTop(self):
        
        if len(self._heap) == 0:
            return False

        headElement = self._heap[0]

        if len(self._heap) == 1:
            self._heap = []
            return headElement

        currentIndex = 0

        self._heap[0] = self._heap[-1]
        self._heap.pop(-1)

        while True:


            leftElement = float('inf')
            rightElement = float('inf')

            leftIndex = currentIndex * 2 + 1
            rightIndex = currentIndex * 2 + 2

            if leftIndex < len(self._heap):
                leftElement = self._heap[leftIndex]

            if rightIndex < len(self._heap):
                rightElement = self._heap[rightIndex]

            currentElement = self._heap[currentIndex]

            if self._heap[currentIndex] > leftElement or self._heap[currentIndex] > rightElement:

                if leftElement > rightElement:

                    ## do right
                    self._heap[currentIndex] = self._heap[rightIndex]
                    self._heap[rightIndex] = currentElement

                    currentIndex = rightIndex

                else:
                    ## do left
                    self._heap[currentIndex] = self._heap[leftIndex]
                    self._heap[leftIndex] = currentElement

                    currentIndex = leftIndex     

                continue

            elif leftElement > self._heap[currentIndex] and rightElement > self._heap[currentIndex]:
                return headElement


        return headElement  

        
import random


a = Heap()


seenSet = set()

for i in range(10000):

    randNum = int(random.random() * 100000)

    if randNum not in seenSet:
        seenSet.add(randNum)

        a.insert(randNum)

print(a.heapSort())
