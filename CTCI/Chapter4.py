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
        self.parent = None

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
    root.left = tree_from_array(array,start,mid-1)
    root.right = tree_from_array(array,mid+1,end)
    return root


"""
4.3 List of depths.
"""

class Solution43:
    def __init__(self):
        self.lists = []

    def create_lists(self,root):
        return self.generate_lists(root,0)

    def generate_lists(self,root,level):
        if not root:
            return None

        list = None
        if len(self.lists) == level:
            list = [root.val]
            self.lists.append(list)
        else:
            list = self.lists[level]
            list.append(root.val)

        self.generate_lists(root.left, level+1)
        self.generate_lists(root.right, level+1)


"""
4.4 Check balanced
"""
#top-down

def depth(root):
    if not root:
        return 0

    return max(depth(root.left), depth(root.right)) + 1

def is_balanced1(root):
    if not root:
        return True

    if abs(depth(root.left) - depth(root.right)) > 1:
        return False

    return is_balanced1(root.left) and is_balanced1(root.right)

#bottom-up

def is_balanced2(root):
    if not root:
        return 0

    left = is_balanced2(root.left)
    if left == -1:
        return -1

    right = is_balanced2(root.right)
    if right == -1:
        return -1

    if abs(left-right) > 1:
        return -1
    else:
        return max(is_balanced2(root.left),is_balanced2(root.right)) + 1


"""
4.5 Validate BST
"""


def is_bst(root,low,high):
    if not root:
        return True

    return root.val > low and root.val < high and is_bst(root.left,low,root.val) and is_bst(root.right,root.val,high)


class Sol44:
    def __init__(self):
        self.val = None


    def is_bst2(self,root):
        if not root:
            return True

        if self.is_bst2(root.left):
            if not self.val or root.val > self.val:
                val = root.val
                return self.is_bst2(root.right)
            else:
                return False
        else:
            return False


"""
4.6 Successor
"""

def successor_node(node):
    if not node:
        return None

    succ = None
    if node.right:
        succ = node.right
        while succ.left:
            succ = succ.left
    else:
        succ = node.parent
        while node == succ.right:
            node = succ
            succ = succ.parent

    return succ


"""
4.7 Build Order
"""

class Sol47:

    def __init__(self,graph):
        self.graph = graph

    def build_order(self):
        self.order = []
        self.visited = set()
        self.partial = set()
        for node in self.graph:
            if node not in self.visited:
                if not self.dfs(node):
                    return None
        return self.order[::-1]

    def dfs(self,node):
        if node in self.partial:
            return False

        for neighbour in self.graph[node]:
            self.partial.add(node)
            if neighbour not in self.visited:
                if not self.dfs(neighbour):
                    return False

        self.visited.add(node)
        self.order.append(node)
        return True


"""
4.8 First Common Ancestor
"""

def LCA(root,p,q):
    if not root:
        return None

    if root == p or root == q:
        return root

    L = LCA(root.left, p, q)
    R = LCA(root.right,p, q)

    if L and R:
        return root

    return L or R


"""
4.9 BST Sequences
"""
def weave_lists(first, second, results, prefix=[]):
    # Base Case
    # Check if first or second are empty
    if not first or not second:
        # Prepend prefix
        result = prefix[:]
        result.extend(first)
        result.extend(second)

        # Add to final results
        results.append(result)
        return

    # Remove elements and recurse
    # Use backtracking to put items back
    # Always remove first element of array

    headFirst = first.pop(0)
    prefix.append(headFirst)
    weave_lists(first,second,results,prefix)
    prefix.pop()
    first.insert(0,headFirst)

    headSecond = second.pop(0)
    prefix.append(headSecond)
    weave_lists(first,second,results,prefix)
    prefix.pop()
    second.insert(0,headSecond)

def allSequences(root):
    # All results stored here
    result = []
    # Base case, no node.
    if not root:
        result.append([])
        return result

    # We are going to use the value of the current node as
    # a prefix to the arrays from the subtrees that are going to be weaved.
    prefix = [root.val]

    # Recurse in subtrees
    leftSequences = allSequences(root.left)
    rightSequences = allSequences(root.right)

    # To try out all possible combinations. Weave together each list from each side.
    for leftSeq in leftSequences:
        for rightSeq in rightSequences:
            # Store weave results
            weaved = []
            weave_lists(leftSeq,rightSeq,weaved,prefix)
            result.extend(weaved)

    return result

"""
4.10 Check subtree T1,T2
"""


def is_subtree(t1, t2):
    if not t1:
        return False

    if t1.val == t2.val and is_match(t1,t2):
        return True

    return is_subtree(t1.left,t2) or is_subtree(t1.right,t2)


def is_match(t1, t2):
    if not t2:
        return True
    if not t1:
        return False

    if t1.val != t2.val:
        return False

    return is_match(t1.left, t2.left) and is_match(t1.right, t2.right)

"""
4.11 Random Node.
"""
import random
class RandomTree:
    def __init__(self,val):
        self.val = val
        self.size = 1 # the current node counts to the size
        self.left = None
        self.right = None

    def insert(self,val):
        if val <= self.val:
            if not self.left:
                self.left = RandomTree(val)
            else:
                self.left.insert(val)
        else:
            if not self.right:
                self.right = RandomTree(val)
            else:
                self.right.insert(val)

        self.size += 1

    def find(self,val):
        if self.val == val:
            return self
        elif self.val < val:
            self.right.find(val)
        else:
            self.left.find(val)


    def getRandomNode(self):
        leftSize = self.left.size if self.left else 0
        index = random.randint(0,leftSize)
        if index < leftSize:
            return self.left.getRandomNode()
        elif index == leftSize:
            return self
        else:
            return self.right.getRandomNode()

"""
4.12 Paths with Sum
"""

class Sol412:

    def count_paths(self, root, target):
        if not root:
            return 0

        root_paths = self.count_node_paths(root, target, 0)

        left = self.count_node_paths(root.left, target, 0)
        right = self.count_node_paths(root.right, target, 0)
        return root_paths + left + right

    def count_node_paths(self, root, target, current):
        if not root:
            return 0

        current += root.val
        total_paths = 0
        if current == target:
            total_paths += 1

        total_paths += self.count_node_paths(root.left, target, current)
        total_paths += self.count_node_paths(root.right, target, current)

        return total_paths
