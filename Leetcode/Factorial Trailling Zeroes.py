class Solution(object):
    def trailingZeroes(self, n):
        zeroes = 0
        while n > 0:
            zeroes += n // 5
            n //= 5
        return zeroes