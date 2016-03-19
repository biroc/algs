class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        if not A:
            return 0
        if len(A) == 1:
            return 1
        so_far = 2
        size = 2
        for i in range(2,len(A)):
            if (A[i] - A[i-1])*(A[i-1]-A[i-2]) > 0:
                so_far += 1
            else:
                so_far = 2
            size = max(size,so_far)

        return size