import random
import pytest

class BinaryHeap:
    def __init__(self):
        self.queue = []
        self.size = 0

    def leftIndex(self, index):
        return (2 * index + 1)

    def rightIndex(self, index):
        return (2 * index + 2)

    def parentIndex(self, index):
        return (index - 1)/2

    def getSize(self):
        return self.size

    def getValue(self, index):
        if index < self.size and index >= 0:
            return self.queue[index]

    def setValue(self, index, val):
        assert index < self.size
        self.queue[index] = val

    def insert(self, key):
        self.queue.append(key)
        self.size += 1
        index = self.size - 1

        cur = self.getValue(index)
        assert cur == key
        while index >= 0:
            cur = self.getValue(index)
            p = self.parentIndex(index)
            pval = self.getValue(p)
            if not pval:
                break
            else:
                if pval > cur:
                    self.setValue(p, cur)
                    self.setValue(index, pval)
                    index = p
                else:
                    break


    def findMin(self):
        if self.size > 0:
            return self.queue[0]

    def _min(self, lval, rval):
        min_val = None
        if lval:
            min_val = lval
        if rval:
            if not min_val:
                min_val = rval
            else:
                min_val = min(rval, min_val)
        return min_val

    def delMin(self):
        if self.size == 0:
            return None

        min_val = self.queue[0]
        self.queue[0] = self.queue[self.size - 1]
        self.size -= 1
        index = 0
        while index < self.size:
            cur = self.getValue(index)
            l = self.leftIndex(index)
            lval = self.getValue(l)
            r = self.rightIndex(index)
            rval = self.getValue(r)
            cmp = self._min(lval, rval)
            if not cmp:
                break
            if cmp == lval:
                if cur > cmp:
                    self.setValue(index, lval)
                    self.setValue(l, cur)
                    index = l
                else:
                    break
            else:
                if cur > rval:
                    assert cmp == rval
                    self.setValue(index, rval)
                    self.setValue(r, cur)
                    index = r
                else:
                    break
        return min_val

    def printHeap(self):
        print self.queue[:self.size]

if __name__ == "__main__":
    keys = range(100)
    random.shuffle(keys)
    print keys
    heap = BinaryHeap()

    for x in keys:
        heap.insert(x)
    min_val = heap.findMin()
    heap.printHeap()

    while heap.getSize() > 0:
        min_val = heap.delMin()
        print "min is ", min_val
        print "heap is :"
        heap.printHeap()

