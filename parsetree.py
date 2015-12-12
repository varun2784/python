class Node:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def setLeft(self, n):
        self.left = n

    def getLeft(self):
        return self.left

    def setRight(self, n):
        self.right = n

    def getRight(self):
        return self.right

    def getValue(self):
        return self.val

    def setValue(self, val):
        self.val = val

    def printNode(self):
        print self.val
        if self.left != None:
            self.left.printNode()
        if self.right != None:
            self.right.printNode()
class Tree:
    def __init__(self, root = None):
        self.root = root

    def printTree(self):
        root = self.root
        root.printNode()
def findOp(expr):
    bracket = 0
    index =  -1
    if not expr:
        return -1
    if expr[1] != '(':
        return 1
    for i in range(1,len(expr)):
        if expr[i] == '(':
            bracket += 1
        if expr[i] == ')':
            bracket -= 1
        if bracket == 0:
            index = i
    return index


def buildTree(expr, parent = None):
    print expr
    if len(expr) == 0:
        return None
    if len(expr) == 1:
        return Node(expr[0])

    print expr
    assert expr[0] == '('
    assert expr[len(expr) - 1] == ')'

    if len(expr) == 5:
        left = Node(expr[1])
        right = Node(expr[3])
        root = Node(expr[2])
        root.setLeft(left)
        root.setRight(right)
        return root

    index = findOp(expr)
    print index
    assert index != -1
    left = buildTree(expr[1: index + 1])
    print(left)
    right = buildTree(expr[index + 2: -1])
    print(right)
    root = buildTree([expr[index + 1]])
    print(root)
    root.setLeft(left)
    root.setRight(right)
    return root

if __name__ == "__main__":
    expr = ['(', '3', '+', '(', '4', '*', '5' ,')',')']
    rootNode = buildTree(expr)
    parseTree = Tree(rootNode)
    parseTree.printTree()
