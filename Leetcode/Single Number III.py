class Solution(object):
    def singleNumber(self, nums):
        mask = self.find_1(nums)
        a = b = 0
        for num in nums:
            if (mask & num) == 0:
                a ^= num
            else:
                b ^= num
        
        return [a,b]
        
    def find_1(self,nums):
        comb = 0
        for num in nums:
            comb ^= num
            
        return comb & (~(comb-1))
        