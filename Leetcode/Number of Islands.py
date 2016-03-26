class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '2': continue
                is_island = self.explore(grid,i,j,m,n)
                if is_island: count += 1

        return count

    def explore(self,grid,row,col,m,n):
        if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == '0':
            return False

        if grid[row][col] == '2':
            return True

        current = True if grid[row][col] == '1' else False
        grid[row][col] = '2'

        above = self.explore(grid,row-1,col,m,n)
        below = self.explore(grid,row+1,col,m,n)
        left = self.explore(grid,row,col-1,m,n)
        right = self.explore(grid,row,col+1,m,n)

        return current or above or below or left or right

        