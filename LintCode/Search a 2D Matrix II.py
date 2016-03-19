class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        if not matrix:
            return 0
        x = 0
        y = len(matrix[0]) - 1
        seen = 0
        while x < len(matrix) and y >= 0:
            current = matrix[x][y]
            if current == target:
                seen += 1
                x += 1
                y -= 1
            elif current > target:
                y -= 1
            else:
                x += 1
        return seen