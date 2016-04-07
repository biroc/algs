class Solution(object):
    def isSymmetric(self, root):
        def sym(left,right):
            if not left and not right: return True
            if (left is None) != (right is None): return False
            return left.val == right.val and sym(left.right,right.left) and sym(left.left,right.right)
        if not root: return True
        return sym(root.left,root.right)
