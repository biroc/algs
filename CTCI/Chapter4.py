class Graph:
    def __init__(self):
        self._graph = {}

    def add_vertex(self,x):
        if x not in self._graph:
            self._graph[x] = []

    def add_vertices(self,vertices):
        for v in vertices:
            self.add_vertex(v)

    def add_edge(self,edge):
        vertex1, vertex2 = tuple(edge)
        if vertex1 in self._graph:
            self._graph[vertex1].append(vertex2)
        else:
            self._graph[vertex1] = [vertex2]

    def add_edges(self,edges):
        for edge in edges:
            self.add_edge(edge)

    def get_edges(self):
        edges = []
        for v in self._graph:
            for neigh in self._graph[v]:
                edges.append(v,neigh)

        return edges

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

"""
4.1 Route between Nodes
"""

def is_route(graph,start,end):
    visited = set()
    queue = [start]
    visited.add(start)
    while queue:
        node = queue.pop(0)
        for neigh in node:
            if neigh not in visited:
                if neigh == end:
                    return True
                else:
                    queue.append(neigh)
                    visited.add(neigh)
    return False

"""
4.2 Minimal tree. Tree from sorted array.
"""

def minimal_tree(array):

    return tree_from_array(array,0,len(array)-1)

def tree_from_array(array,start,end):
    if start > end:
        return None

    mid = (start + end) >> 1
    root = TreeNode(array[mid])
    root.left = tree_from_array(array,start,mid)
    root.right = tree_from_array(array,mid+1,end)
    return root
