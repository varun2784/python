import unittest
import pytest

class Vertex:
    def __init__(self, name):
        self.name = name
        self.out = set()

    def IsConnection(self, name):
        return (name in self.out)

    def AddConnection(self, name):
        assert (name not in self.out)
        self.out.add(name)

    def GetName(self):
        return self.name

    def GetConnections(self):
        return list(self.out)

class Graph:

    def __init__(self):
        self.graph = {}

    def GetVertex(self, name, create):
        if name in self.graph:
            return self.graph[name]
        else:
            if create == True:
                v = Vertex(name)
                self.graph[name] = v
                return v
            else:
                return None

    def AddEdge(self, name1, name2):
        v1 = self.GetVertex(name1, True)
        assert v1 != None
        v2 = self.GetVertex(name2, True)
        assert v2 != None
        v1.AddConnection(name2)
        v2.AddConnection(name1)

    def PrintGraph(self):
        for v in self.graph.values():
            print v.GetName(), v.GetConnections()


def test_graph():
    g = Graph()
    g.AddEdge('a', 'b')
    g.AddEdge('b', 'c')
    g.AddEdge('b', 'd')
    g.AddEdge('d', 'e')
    g.AddEdge('c', 'f')
    g.PrintGraph()
    #assert GetNeighbour(Graph, 'd') == ['b', 'e']
    #print GetIndirectNeighbour_dfs(Graph, 'a')
    #print dfs_iter(Graph, 'a')
    #print dfs_recursive(Graph, 'a')
    #print GetIndirectNeighbour_bfs(Graph, 'a')
    #print GetIndirectNeighbour_dfs(Graph, 'd')
    #print GetIndirectNeighbour_bfs(Graph, 'd')

if __name__ == "__main__":
    test_graph()
