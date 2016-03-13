class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix: return []
        spiral = []
        m, n = len(matrix), len(matrix[0])
        row, col = 0, -1
        while True:
            for i in range(n):
                col += 1
                spiral.append(matrix[row][col])

            m -= 1
            if m == 0: break

            for i in range(m):
                row += 1
                spiral.append(matrix[row][col])

            n -= 1
            if n == 0: break

            for i in range(n):
                col -= 1
                spiral.append(matrix[row][col])

            m -= 1
            if m == 0: break

            for i in range(m):
                row -= 1
                spiral.append(matrix[row][col])

            n -= 1
            if n == 0: break
        return spiral
