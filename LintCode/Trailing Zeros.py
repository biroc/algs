class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        count = 0
        j = 5
        if n == j:
            return 1
        while n // j >= 1:
            count += n // j
            j *= 5

        return count