class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1: return 0
        max_so_far, lowest_so_far = max(prices[1]-prices[0],0), prices[0]
        for i in range(1,len(prices)):
            max_so_far = max(max_so_far,prices[i] - lowest_so_far)
            lowest_so_far = min(lowest_so_far,prices[i])
        return max_so_far
