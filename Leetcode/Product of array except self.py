class Solution(object):
    def productExceptSelf(self, nums):
        running_prod = 1
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] *= running_prod
            running_prod *= nums[i]

        running_prod = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= running_prod
            running_prod *= nums[i]

        return result
        