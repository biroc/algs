class Solution(object):
    def nextPermutation(self, nums):
        k = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                k = i
                break
        if k == -1:
            self.reverse(nums,0,len(nums))
        else:
            l = -1
            for i in range(len(nums)-1,-1,-1):
                if nums[i] > nums[k]:
                    l=i
                    break
            nums[l], nums[k] = nums[k], nums[l]
            self.reverse(nums,k+1,len(nums))

    def reverse(self,nums,start,end):
        for i in range((end-start) // 2):
            nums[start+i], nums[end-i-1] = nums[end-i-1], nums[start+i]