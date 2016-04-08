class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        self.add_leftest(root)

    def add_leftest(self,root):
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        return len(self.stack) != 0

    def next(self):
        smallest = self.stack.pop()
        self.add_leftest(smallest.right)
        return smallest.val