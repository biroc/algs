class Solution(object):
    def canJump(self, nums):
        reach = i = 0
        while i < len(nums) and i <= reach:
            reach = max(reach, i + nums[i])
            i += 1
        return reach >= len(nums)-1


# Alternative solution, looking for 0s.
class Solution(object):
    def canJump(self, nums):
        for i in range(len(nums)-2,-1,-1):
            if nums[i] == 0:
                needed = 1
                j = i
                while needed > nums[j]:
                    needed += 1
                    j -= 1
                    if j < 0: return False
        return True
