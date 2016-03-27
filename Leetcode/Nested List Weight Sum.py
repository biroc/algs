# """
# This is the interface that allows for creating nested lists.
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        self.total = 0
        self.find_total(nestedList,1)
        return self.total

    def find_total(self, nestedList,level):
        for elem in nestedList:
            if not elem.isInteger():
                self.find_total(elem.getList(),level+1)
            else:
                self.total += level * elem.getInteger()
