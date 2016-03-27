class Solution(object):
    def getPermutation(self, n, k):
        factorial = 1
        for i in range(1,n+1):
            factorial *= i

        numbers = []
        for i in range(1,n+1):
            numbers.append(i)

        k -= 1
        res = ''
        for i in range(n):
            factorial //= (n-i)
            index = k // factorial
            k = k % factorial

            res += str(numbers[index])
            numbers.pop(index)

        return res