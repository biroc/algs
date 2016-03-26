class Solution:
    # Right to left
    def permutationIndex(self, A):
        # Write your code here
        index = 1
        factorial = 1
        pos = 2
        for i in range(len(A)-2, -1, -1):
            smaller = 0
            for j in range(i+1, len(A)):
                if A[i] > A[j]:
                    smaller += 1

            index += (smaller * factorial)
            factorial *= pos
            pos += 1

        return index


# Left to right
    def permutationIndex(self, A):
        # Write your code here
        N = len(A) - 1
        factorial = self.factorial(N)
        index = 1
        for i in range(0,len(A)):
            smaller = 0
            for j in range(i+1,len(A)):
                if A[i] > A[j]: smaller += 1

            index += (smaller * factorial)
            if N: factorial //= N
            N -= 1

        return index

    def factorial(self,n):
        if n <= 1:
            return 1
        return n * self.factorial(n-1)