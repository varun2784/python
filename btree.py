import random
import pytest


class kv_pair:
    def __init__(self, k=None, v=None):
        self.k = k
        self.v =v

    def put_k(self, k):
        self.k = k

    def put_v(self,v):
        self.v = v

    def get_k(self):
        return self.k

    def get_v(self):
        return self.v

class BNode:
    def __init__(self, order, leaf=None):
        self.kv = [None] * order
        self.kv_cnt = 0
        self.order = order
        self.childs = [None] * (order + 1)
        self.child_cnt = 0
        self.parent = None
        self.leaf = leaf

    def get_childs(self):
        return self.childs

    def get_kv_index(self, index):
        assert index < self.order
        return self.kv[index]

    def put_kv_index(self, index, kv):
        assert index < self.order
        self.kv[index] = kv

    def put_child_index(self, index, child):
        assert index <= self.order
        self.childs[index] = child

    def get_child_index(self, index):
        return self.childs[index]

    def get_kv(self, k):
        if not self:
            return None
        for i, kv in list(enumerate(self.kv)):
            if kv:
                if kv.get_k() == k:
                    return kv.get_v()
                elif kv.get_k() > k:
                    assert i >= 1
                    child = self.childs[i-1]
                    return child.get_kv(k)
            else:
                break
        return None


    def traverse(self):
        if not self:
            return None
        else:
            for i, kv in list(enumerate(self.kv)):
                if kv:
                    print "(", kv.get_k(), kv.get_v(), ")"
            for child in self.childs:
                if child:
                    child.traverse()


    def put_kv_notfull(self, k, v):
        for i, kv in reversed(list(enumerate(self.kv))):
            #print i, kv
            if kv:
                if kv.get_k() > k:
                    assert not self.kv[i + 1]
                    self.kv[i+1] = kv
                    self.kv[i] = None
                else:
                    assert kv.get_k() != k
                    i += 1
                    break
        assert not self.kv[i]
        self.kv[i] = kv_pair(k, v)
        self.kv_cnt += 1
        assert self.kv_cnt <= self.order
        assert self.leaf == True
        #print list(enumerate(self.kv))


    def split_node(self, k, root):
        assert self.kv_cnt == self.order
        mid = self.order / 2
        if not self.parent:
            parent = BNode(self.order, False)
            child_index = mid
            root = parent
        else:
            parent = self.parent
            for i, child in reversed(list(enumerate(parent.get_childs()))):
                if child:
                    if child == self:
                        child_index = i
                        break
                    else:
                        assert not parent.get_child_index(i + 1)
                        parent.put_child_index(i + 1, child)
                        parent.put_child_index(i, None)
        right = BNode(self.order, self.leaf)
        right.parent = parent
        self.parent = parent
        kv_mid = self.get_kv_index(mid)
        parent.put_kv_index(child_index, kv_mid)

        parent.kv_cnt += 1
        parent.put_child_index(child_index, self)
        parent.put_child_index(child_index + 1, right)
        parent.child_cnt += 2
        self.put_kv_index(mid, None)
        self.kv_cnt -= 1
        for i in range(mid + 1, self.order):
            right.put_kv_index(i - (mid + 1), self.get_kv_index(i))
            right.kv_cnt += 1
            self.kv_cnt -= 1
            self.put_kv_index(i, None)
            right.put_child_index(i - (child_index + 1), self.get_child_index(i))
            right.child_cnt += 1
            self.put_child_index(i, None)
            self.child_cnt -= 1

        if k < kv_mid.get_k():
            return self
        else:
            return right

    def put_kv(self, k, v, root):
        if self.kv_cnt == self.order:
            node = self.split_node(k, root)
            return node.put_kv(k, v, root)
        else:
            if self.leaf == True:
                return self.put_kv_notfull(k, v)
            for i, kv in list(enumerate(self.kv)):
                if kv:
                    assert kv.get_k() != k
                    if kv.get_k() > k:
                        break
                else:
                    break
            child = self.get_child_index(i)
            if child:
                return child.put_kv(k, v, root)
            else:
                node = BNode(self.order, True)
                self.set_child_index(i, node)
                node.parent = self
                return node.put_kv(k, v, root)
                

class BTree:
    def __init__(self, order):
        self.root = None
        self.order = order

    def get(self, k):
        return self.root.get_kv(k)


    def traverse(self):
        self.root.traverse()

    def put(self, k, v=None):
        if not self.root:
            self.root = BNode(self.order, True)

        self.root.put_kv(k, v, self.root)


if __name__ == "__main__":
    keys = range(6)
    random.shuffle(keys)
    btree = BTree(3)
    print keys
    for k in keys:
        print "inserting", k
        btree.put(k)
    btree.traverse()
