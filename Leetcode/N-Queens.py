class Solution(object):
    def solveNQueens(self, n):
        matrix = [['.' for i in range(n)]for j in range(n)]
        result = []
        self.solveQueens(matrix,0,result)
        return result

    def solveQueens(self,matrix,col,result):
        if col == len(matrix):
            list = []
            for row in matrix:
                list.append(''.join(str(r) for r in row))
            result.append(list)
            return

        for i in range(len(matrix)):
            if self.isSafePosition(matrix,i,col):
                matrix[i][col] = 'Q'
                self.solveQueens(matrix,col+1,result)
                matrix[i][col] = '.'

    def isSafePosition(self,matrix,row,col):
        i = 0
        while i < col:
            if matrix[row][i] == 'Q':
                return False
            i += 1
        i = 0
        while row-i >=0 and col-i >=0:
            if matrix[row-i][col-i] == 'Q':
                return False
            i += 1

        i = 0
        while row+i < len(matrix) and col-i >= 0:
            if matrix[row+i][col-i] == 'Q':
                return False
            i += 1
        return True