class Solution(object):
    def maxPathSum(self, root):
        self.maxsum = -999999
        return self.max_sum(root)

    def max_sum(self,root):
        if not root:
            return 0

        left = self.max_sum(root.left)
        right = self.max_sum(root.right)

        self.maxsum = max(self.maxsum,root.val + left + right)
        to_return = root.val + max(left,right)

        return to_return if to_return > 0 else 0
