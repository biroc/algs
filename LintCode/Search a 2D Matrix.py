class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        low = 0
        high = len(matrix)
        while low < high:
            mid = (low+high) // 2
            if target == matrix[mid][0]:
                return True
            if target > matrix[mid][0]:
                low = mid + 1
            else:
                high = mid

        low -= 1
        if low < 0:
            return False

        small = 0
        high = len(matrix[low])

        while small < high:
            mid = (small + high) //2
            if target == matrix[low][mid]:
                return True
            elif target > matrix[low][mid]:
                small = mid + 1
            else:
                high = mid

        return False
        