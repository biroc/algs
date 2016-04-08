class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        lists = []
        self.leveltraverse(root,lists,0)
        return lists

    def leveltraverse(self,root,lists,level):
        if root:
            current = []
            if lists and len(lists) >= level + 1:
                current = lists[level]
                current.append(root.val)
            else:
                current.append(root.val)
                lists.append(current)

            self.leveltraverse(root.left,lists,level+1)
            self.leveltraverse(root.right,lists,level+1)