class Vertex:
    def __init__(self, v):
        self.key = v
        self.connections = {}

    def getKey(self):
        return self.key

    def addConnection(self, key, weight=0):
        if (key not in self.connections):
            self.connections[key] = weight
        else:
            raise Exception("%s already connected to %s" %(self.key, key))

    def removeConnections(self, key):
        if (key not in self.connections):
            raise Exception("%s is not connected to %s" %(self.key, key))
        else:
            del self.connections[key]

    def getConnections(self):
        return self.connections
        

class Graph:
    def __init__(self):
        self.vertices = {}

    def getVertex(self, key):
        if key in self.vertices:
            return self.vertices[key]

    def addVertex(self, key):
        if key not in self.vertices:
            v = Vertex(key)
            self.vertices[key] = v
        else:
            v = self.vertices[key]
        return v

    def addEdge(self, key1, key2, weight=1):
        v1 = self.addVertex(key1)
        v1.addConnection(key2, weight)
        v2 = self.addVertex(key2)
        v2.addConnection(key1, weight)

    def removeEdge(self, key1, key2):
        v1 = self.getVertex(key1)
        v2 = self.getVertex(key2)
        if (v1 and v2):
            v1.removeConnections(key2)
            v2.removeConnections(key1)
        else:
            raise Exception("%s is not connected to %s" %(key1, key2))

    def printGraph(self):
        for key, v in self.vertices.items():
            print key, v.getConnections()
        print "####"

    def dfsIter(self, key):
        v = self.getVertex(key)
        if v == None:
            return []
        stack = [v]
        visited = []
        while stack:
            u = stack.pop()
            if u not in visited:
                visited.append(u)
                for key in u.getConnections():
                    x = self.getVertex(key)
                    if x not in visited:
                        stack.append(x)
        return [x.getKey() for x in visited]

    def bfsIter(self, key):
        v = self.getVertex(key)
        if v == None:
            return []
        stack = [v]
        visited = []
        while stack:
            u = stack.pop(0)
            if u not in visited:
                visited.append(u)
                for key in u.getConnections():
                    x = self.getVertex(key)
                    if x not in visited:
                        stack.append(x)
        return [x.getKey() for x in visited]

    def dfs_path(self, key1, key2):
        v1 = self.getVertex(key1)
        if v1 == None:
            return []
        v2 = self.getVertex(key2)
        if v2 == None:
            return []
        stack = [v1]
        path = []
        while stack:
            u = stack.pop()
            if u not in path:
                path.append(u)
                if u.getKey() == key2:
                    break
                for key in u.getConnections():
                    x = self.getVertex(key)
                    if x not in path:
                        stack.append(x)
        return [x.getKey() for x in path]

if __name__ == "__main__":
    g = Graph()
    g.addEdge('1', '0', 1)
    g.addEdge('1', '2', 1)
    g.addEdge('2', '0', 1)
    g.addEdge('0', '3', 1)
    g.addEdge('3', '4', 1)
    g.printGraph()
    print g.dfsIter('0')
    print g.bfsIter('0')
    print g.dfs_path('0', '1')

