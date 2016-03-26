class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        numbers, results, n = sorted(nums),0,len(nums)
        for i in range(n-2):
            current = numbers[i]
            start = i + 1
            end = n - 1
            while start < end:
                if current + numbers[start] + numbers[end] < target:
                    results += (end - start)
                    start += 1
                else:
                    end -= 1

        return results