class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for i in range(32):
            val = 0
            for num in nums:
                if (num >> i) & 1:
                    val += 1
            if i == 31 and val % 3:
                result -= (1 << 31)
            else:
                result |= (val % 3) << i

        return result