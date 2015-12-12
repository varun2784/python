import pytest

class Node:
    def __init__(self, val):
        self.Val = val
        self.Next = None

    def SetNext(self, n):
        self.Next = n

    def GetNext(self):
        return self.Next

    def GetVal(self):
        return self.Val

class Slist:
    def __init__(self):
        self.Head = None
        self.Size = 0

    def GetSize(self):
        return self.Size

    def GetHead(self):
        return self.Head

    def SetHead(self, n):
        self.Head = n

    def AddList(self, val):
        n = Node(val)
        h = self.GetHead()
        self.SetHead(n)
        n.SetNext(h)
        self.Size += 1

    def SearchList(self, val):
        n = self.GetHead()
        prev = None
        while n != None:
            if n.GetVal() == val:
                return n, prev
            prev = n
            n = n.GetNext()
        return None, None

    def RemoveList(self, val):
        n, parent = self.SearchList(val)
        if n != None:
            if parent == None:
                self.SetHead(n.GetNext())
            else:
                parent.SetNext(n.GetNext())
            self.Size -= 1

    def PrintList(self):
        n = self.GetHead()
        print "Size is", self.GetSize()
        while n != None:
            print n.GetVal(), "--->"
            n = n.GetNext()

    def ReverseList(self):
        print "Reversing"
        prev = None
        n = self.GetHead()
        while n != None:
            print n.GetVal()
            x = n.GetNext()
            n.SetNext(prev)
            prev = n
            n = x
        self.SetHead(prev)

if __name__ == "__main__":
    Sl = Slist()
    for i in range(0, 10):
        Sl.AddList(i)
    Sl.PrintList()
    Sl.ReverseList()
    Sl.PrintList()
    for i in range(0, 10):
        Sl.RemoveList(i)
        Sl.PrintList()


