class Solution(object):
    def maxPathSum(self, root):
        self.maxsum = -999999
        self.max_sum(root)
        return self.maxsum

    def max_sum(self,root):
        if not root:
            return 0

        left = self.max_sum(root.left)
        right = self.max_sum(root.right)

        self.maxsum = max(self.maxsum, left + right + root.val)
        to_return = root.val + max(left,right)
        if to_return > 0:
            return to_return
        else:
            return 0


