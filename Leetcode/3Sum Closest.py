class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        numbers, n = sorted(nums), len(nums)
        closest = nums[0] + nums[1] + nums[2]
        for i in range(n-2):
            current = numbers[i]
            start = i + 1
            end = n - 1
            while start < end:
                sum = current + numbers[start] + numbers[end]
                close = abs(target - sum)
                if close < abs(target-closest):
                    closest = sum
                if sum > target:
                    end -= 1
                else:
                    start += 1

        return closest