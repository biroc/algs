#Top-down
class Solution(object):
    def uniquePaths(self, m, n):
        self.paths = [[-1 for i in range(m+1)]for j in range(n+1)]
        return self.search_paths(0,0,m,n)

    def search_paths(self,row,col,m,n):
        if row == n-1 and col == m-1:
            return 1

        if row >= n or col >= m:
            return 0

        if self.paths[row+1][col] == -1:
            self.paths[row+1][col] = self.search_paths(row+1,col,m,n)
        if self.paths[row][col+1] == -1:
            self.paths[row][col+1] = self.search_paths(row,col+1,m,n)
            

        return self.paths[row+1][col] + self.paths[row][col+1]

#Bottom-up
class Solution(object):
    def uniquePaths(self, m, n):
        self.paths = [[0 for i in range(n+1)] for j in range (m+1)]
        self.paths[m-1][n] = 1
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                self.paths[row][col] = self.paths[row+1][col] + self.paths[row][col+1]

        return self.paths[0][0]
