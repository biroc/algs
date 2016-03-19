class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        if m == 0: return 0
        n = len(obstacleGrid[0])
        paths = [[0 for i in range(n+1)] for j in range(m+1)]
        paths[m-1][n] = 1
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                paths[row][col] = 0 if obstacleGrid[row][col] == 1 else paths[row+1][col] + paths[row][col+1]

        return paths[0][0]