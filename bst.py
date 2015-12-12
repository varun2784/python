import pytest
from random import shuffle

class BSTnode:
    def __init__(self, key, val, parent=None, left=None, right=None):
        self.key = key
        self.value = val
        self.parent = parent
        self.right = None
        self.left = None

    def __str__(self):
        if self != None:
            return "<" + str(self.key) + " " + str(self.value) + ">"
        else:
            return "None"

    def GetKey(self):
        return self.key

    def GetLeft(self):
        return self.left

    def GetRight(self):
        return self.right

    def GetValue(self):
        return self.value

    def GetParent(self):
        return self.parent

    def SetLeft(self, left):
        self.left = left

    def SetRight(self, right):
        self.right = right

    def SetValue(self, value):
        self.value = value

    def SetParent(self, value):
        self.parent = value

    def SetKey(self, value):
        self.key = value


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def GetSize(self):
        return self.size

    def Get(self, key):
        node, parent = self._search(key, self.root, self.root)
        if node:
            return node.GetValue()
        else:
            return None

    def _search(self, key, cur, parent):
        if (cur == None):
            return None, parent
        if cur.key == key:
            return cur, parent
        elif cur.key < key:
            return self._search(key, cur.GetRight(), cur)
        else:
            return self._search(key, cur.GetLeft(), cur)


    def Put(self, key, value):
        node, parent = self._search(key, self.root, self.root)
        if node == None:
            self.size+=1
            node = BSTnode(key, value, parent)
            if parent == None:
                assert self.size == 1
                self.root = node
            elif parent.GetKey() > key:
                assert parent.GetLeft() == None
                parent.SetLeft(node)
                node.SetParent(parent)
            else:
                assert parent.GetKey() < key
                assert parent.GetRight() == None
                parent.SetRight(node)
                node.SetParent(parent)
        else:
            node.SetValue(value)

    def _get_min(self, node):
        assert node != None
        while node.GetLeft():
            node = node.GetLeft()
        return node.GetKey(), node.GetValue()

    def _get_max(self, node):
        assert node != None
        while node.GetRight():
            node = node.GetRight()
        return node.GetKey(), node.GetValue()

    def _delete(self, key, root, root_parent):
        node, parent = self._search(key, root, root_parent)
        if node.GetLeft() == None and node.GetRight() == None:
            if parent == None:
                self.root = None
                assert root_parent == None
                return True
            if parent.GetLeft() == node:
                parent.SetLeft(None)
            else:
                parent.SetRight(None)
            return True

        if node.GetLeft():
            pre_key, pre_value = self._get_max(node.GetLeft())
            self._delete(pre_key, node.GetLeft(), node)
            node.SetKey(pre_key)
            node.SetValue(pre_value)
            return True

        if node.GetRight():
            suc_key, suc_value = self._get_min(node.GetRight())
            self._delete(suc_key, node.GetRight(), node)
            node.SetKey(suc_key)
            node.SetValue(suc_value)
            return True
        return False

    def Delete(self, key):
        if self._delete(key, self.root, None) == True:
            self.size -= 1
        else:
            assert 1 == 1

    def _inOrder(self, node, list_nodes):
        if node == None:
            return
        self._inOrder(node.GetLeft(), list_nodes)
        list_nodes.append((node.GetKey(), node.GetValue()))
        self._inOrder(node.GetRight(), list_nodes)
        return list_nodes

    def InorderTraverse(self):
        return self._inOrder(self.root, [])

    def _levelOrder(self, node, list_level, level):
        if node == None:
            return
        if level not in list_level:
            list_level[level] = []
        list_level[level].append((node.GetKey(), node.GetValue()))
        self._levelOrder(node.GetLeft(), list_level, level + 1)
        self._levelOrder(node.GetRight(), list_level, level + 1)
        return list_level

    def LevelOrderTraverse(self):
        list_level = self._levelOrder(self.root, {}, 0)
        return list_level

if __name__ == "__main__":
    input = [x for x in range(0, 10)]
    print input
    shuffle(input)
    print input
    Tree = BST()
    for x in input:
        Tree.Put(x, str(x)+"_")
    print "Level Order"
    level_list = Tree.LevelOrderTraverse()
    for i in range(0, len(level_list)):
        print "Level: ", i, level_list[i]
    print "Inorder"
    print Tree.InorderTraverse()
    print Tree.GetSize()
    for x in range(0, 5):
        Tree.Delete(x)
    print "Inorder"
    print Tree.InorderTraverse()
    print "Level Order"
    level_list = Tree.LevelOrderTraverse()
    for i in range(0, len(level_list)):
        print "Level: ", i, level_list[i]
    print Tree.GetSize()

