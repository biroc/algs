class Solution(object):
    def threeSum(self, nums):
        if not nums:
            return []
        numbers, results, n = sorted(nums), [], len(nums)
        for i in range(n-2):
            if not i or numbers[i] > numbers[i-1]:
                target = numbers[i] * -1
                start = i + 1
                end = n - 1
                while start < end:
                    if numbers[start] + numbers[end] == target:
                        results.append([numbers[i],numbers[start],numbers[end]])
                        start += 1
                        end -= 1
                        while start < end and numbers[start] == numbers[start-1]:
                            start += 1
                        while start < end and numbers[end] == numbers[end+1]:
                            end -= 1
                    elif numbers[start] + numbers[end] < target:
                        start += 1
                    else:
                        end -= 1
        return results