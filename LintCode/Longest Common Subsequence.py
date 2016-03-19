class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubsequence(self, A, B):
        m, n = len(A), len(B)
        subs = [[None] * (n+1) for i in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    subs[i][j] = 0
                elif A[i-1] == B[j-1]:
                    subs[i][j] = 1 + subs[i-1][j-1]
                else:
                    subs[i][j] = max(subs[i][j-1],subs[i-1][j])
        
        return subs[m][n]