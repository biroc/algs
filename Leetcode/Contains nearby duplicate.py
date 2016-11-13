class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numbers = set()
        for i, value in enumerate(nums):
            if value in numbers:
                return True
            numbers.add(value)
            if len(numbers) > k:
                numbers.remove(nums[i - k])

        return False