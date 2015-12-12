import unittest
import pytest

Graph = {}

def PrintGraph(graph):
    for u, vSet in sorted(graph.items()):
        print u, list(vSet)

def AddEdge(graph, u, v):
    if u == v:
        return
    if u not in graph:
        graph[u] = set()
    graph[u].add(v)
    if v not in graph:
        graph[v] = set()
    graph[v].add(u)

def RemoveEdge(graph, u, v):
    if v in graph[u]:
        graph[u].remove(v)
    if u in graph[v]:
        graph[v].remove(u)

def GetNeighbour(graph, u):
    if u in graph:
        return sorted(list(graph[u]))
    else:
        return []

def GetIndirectNeighbour_dfs(graph, u):
    visited = set()
    stack = []
    if u in graph:
        stack.append(u)
        while (stack):
            v = stack.pop()
            if v not in visited:
                visited.add(v)
                stack.extend(graph[v] - visited)
        visited.remove(u)
        return sorted(list(visited - graph[u]))
    return []


def GetIndirectNeighbour_bfs(graph, u):
    if u not in graph:
        return []
    queue = []
    visited = set()
    queue.append(u)
    while queue:
        v = queue.pop(0)
        if v not in visited:
            visited.add(v)
            queue.extend(list(graph[v] - visited));
    visited.remove(u)
    return sorted(list(visited - graph[u]))

def dfs_iter(graph, u):
    visited = []
    stack = [u]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for n in graph[v]:
                if n not in visited:
                    stack.append(n)
            #stack.extend(graph[v] - visited)
    return visited

def dfs_recursive(graph, u, visited = None):
    if visited == None:
        visited = [u]

    print u, visited
    for n in graph[u]:
        if n not in visited:
            visited.append(n)
            dfs_recursive(graph, n, visited)
    return visited
#class GraphTests(unittest.TestCase):
#    AddEdge(Graph, 'a', 'a')
#    AddEdge(Graph, 'a', 'b')
#    AddEdge(Graph, 'b', 'c')
#    RemoveEdge(Graph, 'a', 'b')
#    PrintGraph(Graph)
#    print GetNeighbour(Graph, 'a')
#    print GetNeighbour(Graph, 'b')
#
#    def testGetNeighbour1(self):
#        self.assertEqual(GetNeighbour(Graph, 'a'), [])
#
#    def testGetNeighbour2(self):
#        self.assertEqual(GetNeighbour(Graph, 'b'), ['c'])
#
#
#
#if __name__ == "__main__":
#    unittest.main()

def test_graph():
    AddEdge(Graph, 'a', 'b')
    AddEdge(Graph, 'b', 'a')
    AddEdge(Graph, 'b', 'c')
    AddEdge(Graph, 'b', 'd')
    AddEdge(Graph, 'd', 'e')
    AddEdge(Graph, 'c', 'f')
    PrintGraph(Graph)
    assert GetNeighbour(Graph, 'd') == ['b', 'e']
    print GetIndirectNeighbour_dfs(Graph, 'a')
    print dfs_iter(Graph, 'a')
    print dfs_recursive(Graph, 'a')
    print GetIndirectNeighbour_bfs(Graph, 'a')
    print GetIndirectNeighbour_dfs(Graph, 'd')
    print GetIndirectNeighbour_bfs(Graph, 'd')

if __name__ == "__main__":
    test_graph()
