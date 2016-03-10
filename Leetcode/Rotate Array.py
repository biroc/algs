class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        self.reverse(nums,0,len(nums)-k)
        self.reverse(nums,len(nums)-k,len(nums))
        self.reverse(nums,0,len(nums))

        print(nums)
        
    def reverse(self,nums,start,finish):
        for i in range((finish - start) // 2):
            nums[start+i], nums[finish - i - 1] = nums[finish - i - 1], nums[start+i]
        